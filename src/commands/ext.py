import click
from src.services.ext_functions import *

class Context:
    def __init__(self, type, path):
        self.type = type
        self.path = path

@click.command()
@click.option("-t", "--type", type=str, help = "Type of extension", required=True)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx, type, path):
    """Organize files based on extension"""
    ctx.obj = Context(type, path)
    extension = ctx.obj.type
    folder_to_track = ctx.obj.path

        
