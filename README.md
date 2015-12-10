# Alfe, the code butler

A tool that parses TODOs from your source code.

**Currently in development.**

![alfe-snap](https://cloud.githubusercontent.com/assets/13040597/11715950/e3632f46-9f4e-11e5-9027-390a8427f3a3.png)

Allows you to
* search separate files or entire directories with ease
* specify language extension to search
* specify language extension to exclude from search

## Supported file extensions

Alfe will only search files of the following extensions:

.cpp|.cs|.c|.h|.css|.cjsx|.coffee|.ejs|
.erl|.go|.html|.htm|.hbs|.handlebars|
.hs|.hng|.hogan|.jade|.js|.es|.es6|.jsx|
.less|.mustache|.php|.pl|.pm|.py|.rb|
.sass|.scss|.sh|.zsh|.bash|.styl|.twig|.ts


#### Installation

Clone, cd, and pip3 install .

## Usage

#### How to use the CLI:

alfe | option | directory/file


Options are:
* -o --only searches only files of this extension
* -x --exclude searches all other files except this extension

#### Examples

To search only Python files in current directory:
```bash
alfe -o .py .
```

To search all files in a directory:
```bash
alfe Projects/web-app/
```

To search a single file:
```bash
alfe contact.html
```
