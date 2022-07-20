import subprocess
import os
import shlex
import shutil
import win32file
import pywintypes

def changeFileCreateTime(path, ctime):
    handle = win32file.CreateFile(path, win32file.GENERIC_WRITE , 0 , None , win32file.OPEN_EXISTING , 0 , 0)
    PyTime = pywintypes.Time(ctime)
    win32file.SetFileTime(handle,PyTime)

path = "D:/Test"
dir = os.path.join(path, '2022')

def makeFiles():
    """
    ├── D:/
    │   ├── Test/
            │── file.txt 4/30/2022
            │── file (1).txt 4/30/2021
            │── 2022
                │── file.txt 4/30/2022
    """
    os.mkdir(path)
    with open(os.path.join(path, 'file.txt'), mode='a'): pass
    with open(os.path.join(path, 'file (1).txt'), mode='a'): pass
    changeFileCreateTime(os.path.join(path, 'file.txt'), 1651320922)
    changeFileCreateTime(os.path.join(path, 'file (1).txt'), 1619784922)
    os.mkdir(dir)
    with open(os.path.join(dir, 'file.txt'), mode='a'): pass
    changeFileCreateTime(os.path.join(dir, 'file.txt'), 1651320922)

def year():
    cmd = "Categorize year --path D:/Test --verbose"
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
            │── 2022
                │── file.txt 4/30/2022
                │── file.txt (1) 4/30/2022
            │── 2021
                │── file (1).txt 4/30/2021
    """
    files = []
    expected = ['2021', '2022']
    for file in os.listdir(path):
        files.append(file)
    assert check_if_equal(files, expected)

def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def test_main():
    makeFiles()
    year()
    check_files()
    shutil.rmtree(path)

if __name__ == "__main__":
    test_main()
    pass
