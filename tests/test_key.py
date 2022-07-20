import subprocess
import os
import shlex
import shutil

path = "D:/Test"
files_in_test = ['keyword.txt', 'keyword (1).txt', 'text.txt', 'text (1).txt']
dir = os.path.join(path, 'keyword')

def makeFiles():
    """
    ├── D:/
    │   ├── Test/
            │── keyword.txt
            │── keyword (1).txt
            │── text.txt
            │── text (1).txt
            │── keyword
                │── keyword.txt
    """
    os.mkdir(path)
    for file in files_in_test:
        with open(os.path.join(path, file), mode='a'): pass
    os.mkdir(dir)
    with open(os.path.join(dir, 'keyword.txt'), mode='a'): pass

def key():
    cmd = "Categorize key --keyword keyword --path D:/Test --verbose"
    cmdList=shlex.split(cmd)
    try:
        subprocess.run(cmdList, check=True, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as error:
        print(error.stdout)
        print(error.stderr)
        raise error
    cmd = "Categorize key -k text -p D:/Test"
    cmdList=shlex.split(cmd)
    try:
        subprocess.run(cmdList, check=True, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as error:
        print(error.stdout)
        print(error.stderr)
        raise error

def check_files():
    """
    expected
    ├── D:/
    │   ├── Test/
            │── keyword
                │── keyword.txt
                │── keyword (1).txt
                │── keyword (2).txt
            │── text
                │── text.txt
                │── text (1).txt
    """
    files = []
    expected = ['text', 'keyword']
    for file in os.listdir(path):
        files.append(file)
    assert check_if_equal(files, expected)

def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def test_main():
    makeFiles()
    key()
    check_files()
    shutil.rmtree(path)

if __name__ == "__main__":
    test_main()
    pass
