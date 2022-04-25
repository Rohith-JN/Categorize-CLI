import os
import click

from src.Categorize_CLI.common.extensions import *
from src.Categorize_CLI.services.ext_functions import *
from src.Categorize_CLI.services.key_functions import *
from src.Categorize_CLI.services.year_functions import *
 

class Context:
    def __init__(self, type, all, keyword, year, path):
        self.type = type
        self.all = all
        self.keyword = keyword
        self.year = year
        self.path = path

@click.command()
@click.option("-t", "--type", type=str, help = "Type of extension", required=False)
@click.option("-a", "--all", is_flag = True, help = "Organize all files based on keyword", required = False)
@click.option("-k", "--keyword", type=str, help = "Keyword to categorize files", required=False)
@click.option("-y", "--year", is_flag = True, help = "Organize files based on year", required=False)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx, type, all, keyword, year, path):
    """Welcome to Categorize!"""

    

