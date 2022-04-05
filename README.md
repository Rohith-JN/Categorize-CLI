# Categorize-CLI

![](https://img.shields.io/pypi/v/Categorize-CLI?color=blue&style=flat-square) ![](https://img.shields.io/github/license/Rohith-JN/Categorize-CLI?color=green&style=flat-square)

Categorize-CLI is a command-line-tool made using python to organize files in a given directory based on categories like
extension, keyword, creation time, etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Categorize-CLI.

```
pip install Categorize-CLI
```

## Usage

### Safe
Running this command will organize all media files in the working directory

```
Categorize safe
```

### Extensions:
Running this command will organize the files based on the command specified in the working directory

```
Categorize ext -t [command]
```

```
Categorize ext --type [command]
```

Running this command will organize all the files based on extension in the working directory

```
Categorize ext-all
```

Commands:

```
[text, image, audio, video, word, powerpoint, excel, access, executables, pdf, archives, documents, media, safe]
```

### Keyword:
Running this command will organize the files based on the common keyword present in the file names in the working directory

```
Categorize key-all
```

Running this command will organize the files based on the specified keyword present in the file names in the working directory

```
Categorize key -k "keyword"
```

### Creation time:

This command will organize files based on year created in the working directory

```
Categorize year
```

### Other

```
Categorize [command] --help
```
If you do not want to organize files in the working directory and want to organize files in another path then you can just specify the path using this option `-p` or `--path`

```
Categorize [command] --path "path"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)