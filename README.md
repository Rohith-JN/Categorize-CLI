# Categorize-CLI

![](https://img.shields.io/pypi/v/Categorize-CLI?color=blue&style=flat-square) ![](https://img.shields.io/github/license/Rohith-JN/Categorize-CLI?color=green&style=flat-square)
[![Downloads](https://static.pepy.tech/personalized-badge/categorize-cli?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/categorize-cli)

Categorize-CLI is a command-line-tool to help you organize files in a given directory based on categories like
extension, keyword, year-created, etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Categorize-CLI.

```
pip install Categorize-CLI
```

## Usage

### Safe
This command will organize all media files in the working directory

```
Categorize safe
```

### Extensions:
This command will organize the files based on the command specified in the working directory

```
Categorize ext -t [command]
```

```
Categorize ext --type [command]
```

This command will organize all the files based on extension in the working directory

```
Categorize ext-all
```

Commands:

```
[text, image, audio, video, word, powerpoint, excel, access, executables, pdf, archives, documents, media, safe]
```

### Keyword:
This command will organize the files based on the common keyword present in the file names in the working directory

```
Categorize key-all
```

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

### Other

Run this command to get more info on the `commands` and its `options`

```
Categorize [command] --help
```

If you do not want to organize files in the working directory and want to organize files in another path then you can just specify the path using this option `-p` or `--path`

```
Categorize [command] --path "path"
```

## Contributing
[Open a pull request](https://github.com/Rohith-JN/Categorize-CLI/pulls)

[Report an issue](https://github.com/Rohith-JN/Categorize-CLI/issues)

## License
[MIT](https://choosealicense.com/licenses/mit/)
