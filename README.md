# Categorize-CLI

Categorize-CLI is a command-line-tool made using python to organize files in a given directory based on categories like
extension, keyword, creation time, etc.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Categorize-CLI.

```
pip install Categorize-CLI
```

## Usage

### Extensions:
Running this command will organize the files based on the command specified
```
Categorize --ext [Command]
```
This command does the same as above but in the directory or path specified
```
Categorize --ext [Command] "path" will organize files in the given path
```
Commands:
```
[text, image, audio, video, word, powerpoint, excel, access, executables, pdf, archives, documents]
```
### Keyword:
Running this command will organize the files based on the common keyword present in the file names
```
Categorize --key
```
Running this command will organize the files based on the specified keyword present in the file names
```
Categorize --key "keyword"
```
This command does the same as above but in the directory or path specified
```
Categorize --key "keyword" "path" will organize files in the given path
```

### Creation time:
This command will organize files based on which year it was created
```
Categorize --year
```
This command does the same as above but in the directory or path specified
```
Categorize --year "path" 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)