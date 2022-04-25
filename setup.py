from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(

    name='Categorize-CLI',
    version='1.0.0',
    description='Categorize-CLI is a command-line-tool made to help you categorize/organize files in a given directory',
    url="https://github.com/Rohith-JN/Categorize-CLI",
    author="Rohith Nambiar",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    license= "MIT",
    author_email='rohithnambiar04@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Operating System :: Microsoft :: Windows'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Changelog" : "https://github.com/Rohith-JN/Categorize-CLI/blob/main/CHANGELOG.md",
        "Issues": "https://github.com/Rohith-JN/Categorize-CLI/issues",
        "Source" : "https://github.com/Rohith-JN/Categorize-CLI"
    },
    install_requires=['Click', 'colorama', 'progress'],

    entry_points=""" 
        [console_scripts] 
        Categorize=src.Categorize_CLI.__main__:main
        """
)