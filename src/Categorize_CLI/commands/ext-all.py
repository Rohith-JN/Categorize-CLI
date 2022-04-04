import click
from src.Categorize_CLI.services.ext_functions import *

class Context:
    def __init__(self, path):
        self.path = path

@click.command()
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx, path):
    """Organize all files based on extension"""
    ctx.obj = Context(path)
    folder_to_track = ctx.obj.path

    if os.path.exists(folder_to_track):
        click.echo(all_extensions_category(folder_to_track))
    else:
        click.echo("{}: does not exist".format(folder_to_track))
