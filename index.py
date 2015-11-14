import glob
import re
import os
import sys

import click
from pkg_resources import require

EXTES = ('.cpp','.cs','.c','.h','.css','.cjsx','.coffee','.ejs','.erl','.go',
        '.html','.htm','.hbs','handlebars','.hs','.hng','.hogan','.jade',
        '.js','.es','.es6','.jsx','.less','.mustache','.php','.pl','.pm',
        '.py','.rb','.sass','.scss','.sh','.zsh','.bash','.styl','.twig','.ts',)


def lang_option(files, lang=EXTES):

    lang_specific = []

    if lang not in EXTES and lang is not EXTES:
        print('Unsupported file extension', lang)
    for f in files:
        if f.endswith(lang):
            lang_specific.append(f)
    return lang_specific


def where(path):
    """ Finds all files topdown the path """

    all_files = []

    for root, dirs, files in os.walk(path):
        files = lang_option(files, lang=EXTES)
        dirs[:] = [d for d in dirs if not d[0] == '.']

        for name in files:
            if not name.startswith('.'):
                # print(os.path.join(root, name))
                all_files.append(os.path.join(root, name))


    return all_files


def pretty_print(linenum, todo):
    """ Prints a table with all the found todos """

    comm_endings = ['"""', "'''", '*/', '-->', '#}', '--}}', '}}', '%>']
    for i in comm_endings:
        if todo.endswith(i):
            todo = todo[:-len(i)]
    print('   line', linenum.rjust(4), '>>\t', todo )



def search_todo(path):
    """ Extracts a todo from file, feeds todos in printing function """

    all_files = where(path)
    for files in all_files:

        f = open(os.path.abspath(files), 'r', encoding='utf-8')
        printed = False
        for n, row in enumerate(f.readlines()):

            todo = re.compile('\\bTODO\\b.*')
            found = todo.search(row)
            if found:
                if not printed:
                    print('\n',files)
                    printed = True
                pretty_print(str(n+1), found.group())



@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, help='Return the current version.')
# @click.option('-x', '--ext', nargs=2)
@click.argument('path')
def cli(version, path):
    """ extract comment tags from source files """

    search_todo(path)

    if version:
        print(require('alfred')[0].version)
