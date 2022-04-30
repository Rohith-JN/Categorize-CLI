import subprocess

def test_command():
    try:
        subprocess.run(['Categorize'], check=True, capture_output=True, text=True, shell=True)
    except subprocess.CalledProcessError as error:
        print(error.stdout)
        print(error.stderr)
        raise error

if __name__ == '__main__':
    test_command()
