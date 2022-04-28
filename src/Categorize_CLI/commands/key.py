import click
from src.Categorize_CLI.services.key_functions import *
from colorama import init
from colorama import Fore

init()

class Context:
    def __init__(self, keyword, path, verbose):
        self.keyword = keyword
        self.path = path
        self.verbose = verbose

@click.command()
@click.option("-k", "--keyword", type=str, help = "Keyword to categorize files", required=True)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.option("-v", "--verbose", is_flag = True, help = "Show complete output", required = False, default = False)
@click.pass_context
def main(ctx, keyword, path, verbose):
    """Organize files based on specified keyword"""
    ctx.obj = Context(keyword, path, verbose)
    keyword = ctx.obj.keyword
    folder_to_track = ctx.obj.path
    verbose = ctx.obj.verbose

    if os.path.exists(folder_to_track):
        click.echo(specific_name_category(keyword, folder_to_track, verbose))
    elif not os.path.exists(folder_to_track):
        click.echo(os.linesep + Fore.RED + "Error: {} does not exist".format(folder_to_track) + os.linesep)
    
  