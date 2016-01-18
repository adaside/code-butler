![alfe](https://cloud.githubusercontent.com/assets/13040597/12249698/0a2f7d84-b8ca-11e5-8b40-4b6b63ccb086.png)


![version](https://img.shields.io/pypi/v/alfe.svg)

**A tool that parses TODOs from your source code effectively.**

**Currently in beta.**

Alfe is a CLI productivity tool that saves you time by finding all the TODOs and FIXMEs in your code. It tries its best not to bother with files which may not be yours by filtering out gitignore material when searching inside git repositories. The search is very flexible as you can specify either a file or a directory with a relative or absolute path. There are options for searching only one specific file extension or excluding one.

![alfesnap](https://cloud.githubusercontent.com/assets/13040597/12396617/1d5f8fba-be11-11e5-8c91-5f208c6d5e4c.png)

**With Alfe you can**
* search separate files or entire directories with ease
* specify language extension to search
* specify language extension to exclude from search
* search inside git repositories excluding gitignore material
* search by either relative or absolute path

## Supported file extensions

.cpp|.cs|.c|.h|.css|.cjsx|.coffee|.ejs|
.erl|.go|.html|.htm|.hbs|.handlebars|
.hs|.hng|.hogan|.jade|.js|.es|.es6|.jsx|
.less|.mustache|.php|.pl|.pm|.py|.rb|
.sass|.scss|.sh|.zsh|.bash|.styl|.twig|.ts


#### Installation

```
pip3 install alfe
```

## Usage

#### How to use the CLI:

alfe | option | directory/file


Options are:
* **-o --only** searches only files of this extension
* **-x --exclude** searches all other files except this extension

#### Examples

To search all files in a directory:
```bash
alfe Projects/web-app/
```

To search only Python files in current directory:
```bash
alfe -o .py .
```

To search a single file:
```bash
alfe contact.html
```

##License

MIT
