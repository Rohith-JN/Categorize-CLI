import subprocess
import os
import shlex
import shutil

path = "D:/Test"
files_in_test = ['image.jpeg', 'image.jpg', 'text.txt', 'text.png']
dir_1 = os.path.join(path, 'png')
dir_2 = os.path.join(path, 'jpeg')

def makeFiles():
    """
    ├── D:/
    │   ├── Test/
            │── image.jpeg
            │── image.jpg
            │── text.txt
            │── text.png
            │── png
                │── text.png
                │── text (1).png
            │── jpeg
                │── image.jpeg
    """
    os.mkdir(path)
    for file in files_in_test:
        with open(os.path.join(path, file), mode='a'): pass
    os.mkdir(dir_1)
    with open(os.path.join(dir_1, 'text.png'), mode='a'): pass
    with open(os.path.join(dir_1, 'text (1).png'), mode='a'): pass
    os.mkdir(dir_2)
    with open(os.path.join(dir_2, 'image.jpeg'), mode='a'): pass

def ext():
    cmd = "Categorize ext --path D:/Test --verbose --all"
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
            │── png
                │── text.png
                │── text (1).png
                │── text (2).png
            │── jpeg
                │── image.jpeg
                │── image (1).jpeg
            │── txt
                │── text.txt
            │── jpg
                │── image.jpg
    """
    files = []
    expected = ['jpeg', 'jpg', 'png', 'txt']
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
