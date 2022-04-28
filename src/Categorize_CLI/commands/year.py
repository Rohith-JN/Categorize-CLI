import click
from src.Categorize_CLI.services.year_functions import *
from colorama import init
from colorama import Fore

init()

class Context:
    def __init__(self, path, verbose):
        self.path = path
        self.verbose = verbose

@click.command()
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.option("-v", "--verbose", is_flag = True, help = "Show complete output", required = False, default = False)
@click.pass_context
def main(ctx, path, verbose):
    """Organize files based on year created"""
    ctx.obj = Context(path, verbose)
    folder_to_track = ctx.obj.path
    verbose = ctx.obj.verbose

    if os.path.exists(folder_to_track):
        click.echo(year_category(folder_to_track, verbose))
    elif not os.path.exists(folder_to_track):
        click.echo(os.linesep + Fore.RED + "Error: {} does not exist".format(folder_to_track) + os.linesep)
    
