# Alfe, the code butler

An open source tool that finds TODOs in your code.

**Currently in development.**

Allows you to
* search separate files or entire directories
* specify language extension to search


## Usage

pip3 install

```
alfe option directory/file
```

Options are:
* -o --only searches only files of this extension
* -x --exclude searches all other files except this extension


To search only Python files in current directory
```bash
alfe -o .py .
```

To search all files in a directory
```bash
alfe Projects/web-app/
```
