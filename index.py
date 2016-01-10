import glob
import re
import os
import sys
import fnmatch

import click
from pkg_resources import require

EXTES = ('.cpp','.cs','.c','.h','.css','.cjsx','.coffee','.ejs','.erl','.go',
        '.html','.htm','.hbs','.handlebars','.hs','.hng','.hogan','.jade',
        '.js','.es','.es6','.jsx','.less','.mustache','.php','.pl','.pm',
        '.py','.rb','.sass','.scss','.sh','.zsh','.bash','.styl','.twig','.ts',)

COUNTER = 0
F_COUNTER = 0
SEARCHED = 0


def filter_files(files, lang=EXTES):
    """ Filters files according to options or the extes """

    lang_specific = []

    for f in files:
        if f.endswith(lang):
            lang_specific.append(f)
    return lang_specific


def get_gitignore(path):
    """ Searches for gitignore file in parent directories """

    if '.gitignore' in os.listdir(path):
         return parse_gitignore(os.path.join(path, '.gitignore'))
    else:
        if os.path.abspath(path) == '/':
            return
        path = os.path.join('..', path)
        get_gitignore(path)



def parse_gitignore(gipath):
    """ Returns a list with gitignore content """

    gitignore_file = open(os.path.abspath(gipath), 'r')
    gilist = []
    for row in gitignore_file.readlines():
        if not row.startswith('#') and row != '\n':
            if row.endswith('/\n'):
                gilist.append(row[:-2])
            else:
                gilist.append(row[:-1])
    gitignore_file.close()
    return gilist


def get_files(path):
    """ Finds all files topdown the path excluding gitignore material """

    # In case path is singular file:
    if os.path.isfile(path):
        return [path]

    all_files = []
    gilist = get_gitignore(path)
    print(gilist)

    # In case path is directory:

    if not gilist:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d[0] != '.']
            if '.gitignore' in os.listdir(root):
                gilist = parse_gitignore(os.path.join(root, '.gitignore'))
                path = root
                break

            for name in files:
                if not name.startswith('.'):
                    all_files.append(os.path.join(root, name))

    if gilist:
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d[0] != '.' and d not in gilist]

            for item in gilist:
                if fnmatch.fnmatch(root, item):
                    break

            else:
                ignore = []

                for name in files:
                    for item in gilist:
                        if fnmatch.fnmatch(name, item):
                            ignore.append(name)

                    if not name.startswith('.') and name not in ignore:
                        all_files.append(os.path.join(root, name))
    print ('ALL', all_files)
    return all_files


def pretty_print(linenum, todo):
    """ Prints a table with all the found todos """

    global COUNTER
    comm_endings = ['"""', "'''", '*/', '-->', '#}', '--}}', '}}', '%>']
    for i in comm_endings:
        if todo.endswith(i):
            todo = todo[:-len(i)]
    print('   line', linenum.rjust(4), '>>\t', todo )
    COUNTER += 1


def search_todo(filtered_files):
    """ Extracts a todo from file, feeds todos in printing function """

    global F_COUNTER
    global SEARCHED

    for files in filtered_files:
        f = open(os.path.abspath(files), 'r')
        printed = False
        SEARCHED += 1
        for n, row in enumerate(f.readlines()):

            todo = re.compile('\\bTODO\\b.*')
            found = todo.search(row)
            if found:
                if not printed:
                    print('\n',files)
                    printed = True
                    F_COUNTER += 1
                pretty_print(str(n+1), found.group())
        f.close()


def report():
    """ Prints a report at the end of the search """

    global COUNTER
    print('\n\t-=-=-=-\n')
    print('Searched {0} files'.format(SEARCHED))
    print('Found {0} TODOs in {1} files'.format(COUNTER, F_COUNTER))




@click.group(invoke_without_command=True)
@click.option('-v', '--version', is_flag=True, help='Return the current version.')
@click.option('-o', '--only', type=click.Choice(EXTES), help='Specify language extensions to search.')
@click.option('-x', '--exclude', type=click.Choice(EXTES), help='Specify extensions to exclude from search.')
@click.argument('path', required=False)
def cli(version, path, only, exclude):
    """ extract comment tags from source files """

    if path:
        files = get_files(path)

        if only:
            filtered_files = filter_files(files, only)
        elif exclude:
            filtered_files = filter_files(files, tuple(x for x in EXTES if x != exclude))
        else:
            filtered_files = filter_files(files)

        search_todo(filtered_files)
        report()

    if version:
        print(require('alfe')[0].version)
