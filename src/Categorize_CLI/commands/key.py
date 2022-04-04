import click
from src.Categorize_CLI.services.key_functions import *

class Context:
    def __init__(self, keyword, path):
        self.keyword = keyword
        self.path = path

@click.command()
@click.option("-k", "--keyword", type=str, help = "Keyword to categorize files", required=True)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx, keyword, path):
    """Organize files based on specified keyword"""
    ctx.obj = Context(keyword, path)
    keyword = ctx.obj.keyword
    folder_to_track = ctx.obj.path

    if os.path.exists(folder_to_track):
        click.echo(specific_name_category(keyword, folder_to_track))
    else:
        click.echo("{}: does not exist".format(folder_to_track))
    
