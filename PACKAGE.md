<h1 align = "center">Categorize-CLI<h1>

![](https://img.shields.io/pypi/v/Categorize-CLI?color=blue&style=flat-square) ![](https://img.shields.io/github/license/Rohith-JN/Categorize-CLI?color=green&style=flat-square)
[![Downloads](https://static.pepy.tech/personalized-badge/categorize-cli?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/categorize-cli)


Categorize-CLI is a command-line-tool to help you organize files in a given directory based on categories like
extension, keyword, year-created, etc.
 
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
Categorize key -k "keyword"
```
```
Categorize key --keyword "keyword"
```

### Year-created:

This command will organize files based on year created in the working directory

```
Categorize year
```

If you do not want to organize files in the working directory and want to organize files in another path then you can just specify the path using this option `-p` or `--path`

```
Categorize [command] --path "path"
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