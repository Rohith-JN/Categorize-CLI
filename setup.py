from setuptools import setup, find_packages
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(

    name='Categorize-CLI',
    version='0.3.0',
    description='Categorize-CLI is a command-line-tool made using python to organize files in a given directory',
    url="https://github.com/Rohith-JN/Categorize-CLI",
    author="Rohith Nambiar",
    packages=find_packages(),
    include_package_data=True,
    author_email='rohithnambiar04@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/Rohith-JN/Categorize-CLI/issues"
    },
    install_requires=['Click', 'colorama', 'progress'],

    entry_points=""" 
        [console_scripts] 
        Categorize=src.main:main
        """
)