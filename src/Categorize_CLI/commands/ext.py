import click
from src.Categorize_CLI.common.extensions import extensions
from src.Categorize_CLI.services.ext_functions import *

class Context:
    def __init__(self, type, path, all):
        self.type = type
        self.path = path
        self.all = all

@click.command()
@click.option("-t", "--type", type=str, help = "Type of extension", required=False)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.option("-a", "--all", is_flag = True, help = "Organize all files?", required = False, default = False)
@click.pass_context
def main(ctx, type, path, all):
    """Organize files based on specified extension (ex: image, video)"""
    ctx.obj = Context(type, path, all)
    extension = ctx.obj.type
    folder_to_track = ctx.obj.path
    all = ctx.obj.all

    categories = [key for key, value in extensions.items()]
    if extension in categories and os.path.exists(folder_to_track) and not all:
        click.echo(extension_category(extensions[extension], folder_to_track))
    elif not extension in categories and not all:
        click.echo("{} is not one of the types of extensions".format(extension))
    elif not os.path.exists(folder_to_track):
        click.echo("{}: does not exist".format(folder_to_track))
    elif os.path.exists(folder_to_track) and all:
        click.echo(all_extensions_category(folder_to_track))

