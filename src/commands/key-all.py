import click
from src.services.key_functions import *

class Context:
    def __init__(self, path):
        self.path = path

@click.command()
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx,path):
    """Organize all files based on keyword"""
    ctx.obj = Context(path)
    folder_to_track = ctx.obj.path

    if os.path.exists(folder_to_track):
        click.echo(name_category(folder_to_track))
    else:
        click.echo("{}: does not exist".format(folder_to_track))
    
