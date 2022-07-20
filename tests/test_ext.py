import subprocess
import os
import shlex
import shutil

path = "D:/Test"
files_in_test = ['image.jpeg', 'image.jpg', 'text.txt', 'text.png']
dir = os.path.join(path, 'image')

def makeFiles():
    """
    ├── D:/
    │   ├── Test/
            │── image.jpeg
            │── image.jpg
            │── text.txt
            │── text.png
            │── image
                │── image.jpeg
    """
    os.mkdir(path)
    for file in files_in_test:
        with open(os.path.join(path, file), mode='a'): pass
    os.mkdir(dir)
    with open(os.path.join(dir, 'image.jpeg'), mode='a'): pass

def ext():
    cmd = "Categorize ext --type image --path D:/Test --verbose"
    cmdList=shlex.split(cmd)
    try:
        subprocess.run(cmdList, check=True, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as error:
        print(error.stdout)
        print(error.stderr)
        raise error
    cmd = "Categorize ext --type text --path D:/Test"
    cmdList=shlex.split(cmd)
    try:
        subprocess.run(cmdList, check=True, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as error:
        print(error.stdout)
        print(error.stderr)
        raise error

def check_files():
    files = []
    expected = ['text', 'image']
    for file in os.listdir(path):
        files.append(file)
    assert check_if_equal(files, expected)

def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def test_main():
    makeFiles()
    ext()
    check_files()
    shutil.rmtree(path)

if __name__ == "__main__":
    test_main()
    pass
