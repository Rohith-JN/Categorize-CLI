# Categorize-CLI

![](https://img.shields.io/pypi/v/Categorize-CLI?color=blue&style=flat-square) ![](https://img.shields.io/github/license/Rohith-JN/Categorize-CLI?color=green&style=flat-square)
[![Downloads](https://static.pepy.tech/personalized-badge/categorize-cli?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/categorize-cli)

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
```
Categorize key --keyword "keyword"
```

### Creation time:

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
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Todo

1) Add the total amount of size of files moved as an output
2) Remove random characters that appear in the terminal
3) Make the project compatible with linux
4) Write tests for the project
5) Make a mont-year category for organizing
6) Fix the exceptions in name_category() function