<div align="center">
<h1>Categorize-CLI</h1>
<a href="https://github.com/Rohith-JN/Categorize-CLI/blob/main/LICENSE.txt">
  <img src="https://img.shields.io/github/license/Rohith-JN/Categorize-CLI?color=blue&style=flat-square" title="License">
</a>
<a href="https://pypi.org/project/Categorize-CLI/">
  <img src="https://img.shields.io/pypi/v/Categorize-CLI?color=blue&style=flat-square" title="PyPI Version">
</a>
<p>A command-line-tool to help you organize files in a given directory
</p>

</div>

---
## Installation
Categorize-CLI works on python 3.7 and above

Installation is done via pip.
```commandline
pip install Categorize-CLI
```

## Usage

### Extensions:
This command will organize the files based on the specified extension type (ex: image, audio, video) in the working directory

```
Categorize ext -t [command]
```

```
Categorize ext --type [command]
```

Commands:

```
[text, image, audio, video, word, powerpoint, excel, access, executables, pdf, archives, documents, media, safe]
```

### Keyword:
This command will organize the files based on the specified keyword present in the file names in the working directory

```
Categorize key -k [command]
```
```
Categorize key --keyword [command]
```

### Year-created:

This command will organize files based on year created in the working directory

```
Categorize year
```


### Other
If you want to organize files belonging to another directory then you can just specify the path using this option `-p` or `--path`

```
Categorize [command] --path [command]
```

## Command-line-interface

```
Usage: Categorize [OPTIONS] COMMAND [ARGS]...

  Categorize files based on different categories

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  ext   Organize files based on specified extension (ex: image, video)
  key   Organize files based on specified keyword
  year  Organize files based on year created
```