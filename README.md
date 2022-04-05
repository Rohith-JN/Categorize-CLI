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

### Extensions:
Running this command will organize the files based on the command specified in the working directory
```
Categorize ext -t [command]
```
```
Categorize ext --type [command]
```
This command does the same as above but in the directory or path specified
```
Categorize ext -t [Command] -p "path"
```
```
Categorize ext --type [Command] --path "path" 
```
Running this command will organize all the files based on extension in the working directory
```
Categorize ext-all
```
This command does the same as above but in the directory or path specified
```
Categorize ext-all --path "path" 
```
```
Categorize ext-all --p "path" 
```
Commands:
```
[text, image, audio, video, word, powerpoint, excel, access, executables, pdf, archives, documents, media]
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
This command does the same as above but in the directory or path specified
```
Categorize key-all -p "path"
```
```
Categorize key-all --p "path"
```
```
Categorize key -k "keyword" -p "path" 
```
```
Categorize key -k "keyword" --path "path"
```

### Creation time:
This command will organize files based on year created in the working directory
```
Categorize year
```
This command does the same as above but in the directory or path specified
```
Categorize year -p "path" 
```
```
Categorize year --path "path" 
```
### To get more info on the commands and their options

```
Categorize [command] --help
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)