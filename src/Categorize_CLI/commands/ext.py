import click
from src.Categorize_CLI.common.extensions import extensions
from src.Categorize_CLI.services.ext_functions import *
from colorama import init
from colorama import Fore

init()

class Context:
    def __init__(self, type, path, all, verbose):
        self.type = type
        self.path = path
        self.all = all
        self.verbose = verbose

@click.command()
@click.option("-t", "--type", type=str, help = "Type of extension", required=False)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.option("-a", "--all", is_flag = True, help = "Organize all files based on extension (ex: jpeg)", required = False, default = False)
@click.option("-v", "--verbose", is_flag = True, help = "Show complete output", required = False, default = False)
@click.pass_context
def main(ctx, type, path, all, verbose):
    """Organize files based on specified extension (ex: image, video)"""
    ctx.obj = Context(type, path, all, verbose)
    extension = ctx.obj.type
    folder_to_track = ctx.obj.path
    all = ctx.obj.all
    verbose = ctx.obj.verbose

    categories = [key for key, value in extensions.items()]
    if extension in categories and os.path.exists(folder_to_track) and not all:
        click.echo(extension_category(extensions[extension], folder_to_track, verbose))
    elif not extension in categories and not all and extension != None:
        click.echo(os.linesep + Fore.RED + "Error: {} is not one of the types of extensions".format(extension) + os.linesep)
    elif not os.path.exists(folder_to_track):
        click.echo(os.linesep + Fore.RED + "Error: {} does not exist".format(folder_to_track) + os.linesep)
    elif os.path.exists(folder_to_track) and all:
        click.echo(all_extensions_category(folder_to_track, verbose))
    elif extension == None and not all:
        click.echo(os.linesep + Fore.RED + "Error: Please specify an option" + os.linesep)
