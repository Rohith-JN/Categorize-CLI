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

## Categorize-CLI v1.0.0

A new update aimed to simplify the command-line-interface while increasing functionality

- [View the changelog](https://github.com/Rohith-JN/Categorize-CLI/blob/main/CHANGELOG.md) for all the new features!

## Usage

### Extensions:
This command will organize the files based on the specified extension type (ex: image, audio, video) in the working directory

```
Categorize ext -t [command]
```

```
Categorize ext --type [command]
```

To organize all files based on extension (ex: .jpeg, .txt) use the `--all` flag

```
Categorize ext --all
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

If you want to view the full output you can use the verbose flag `-v` or `--verbose`

```
Categorize [command] --verbose
```

Command line interface

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