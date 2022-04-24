import os
import click

from src.common import extensions
from src.services.ext_functions import *
from src.services.key_functions import *
from src.services.year_functions import *
 

class Context:
    def __init__(self, type, all, keyword, year, path):
        self.type = type
        self.all = all
        self.keyword = keyword
        self.year = year
        self.path = path

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                commands.append(filename.replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"src.Categorize_CLI.commands.{name}", None, None, ["main"])
        except ImportError:
            return
        return mod.main

@click.pass_context
def ext_all(ctx, all):
    """Organize all files based on extension"""
    ctx.obj = Context(all, path)
    all = ctx.obj.all
    path = ctx.obj.path

    if os.path.exists(path) and all:
        click.echo(all_extensions_category(path))
    else:
        click.echo("{}: does not exist".format(path))

@click.pass_context
def ext(ctx, type, path):
    """Organize files based on specified extension"""
    ctx.obj = Context(type, path)
    type = ctx.obj.type
    path = ctx.obj.path

    categories = [key for key, value in extensions.items()]
    if type in categories and os.path.exists(path):
        click.echo(extension_category(extensions[type], path))
    elif not type in categories:
        click.echo("{} is not one of the types of extensions".format(type))
    elif not os.path.exists(path):
        click.echo("{}: does not exist".format(path))

@click.pass_context
def key(ctx, keyword, path):
    """Organize files based on specified keyword"""
    ctx.obj = Context(keyword, path)
    keyword = ctx.obj.keyword
    path = ctx.obj.path

    if os.path.exists(path):
        click.echo(specific_name_category(keyword, path))
    else:
        click.echo("{}: does not exist".format(path))

@click.pass_context
def year(ctx, year, path):
    """Organize files based on year created"""
    ctx.obj = Context(year, path)
    year = ctx.obj.year
    path = ctx.obj.path

    if os.path.exists(path) and year:
        click.echo(year_category(path))
    else:
        click.echo("{}: does not exist".format(path))
    

@click.command()
@click.option("-t", "--type", type=str, help = "Type of extension", required=False, callback=ext)
@click.option("-a", "--all", is_flag = True, help = "Organize all files based on keyword", required = False, callback=ext_all)
@click.option("-k", "--keyword", type=str, help = "Keyword to categorize files", required=False, callback=key)
@click.option("-y", "--year", is_flag = True, help = "Organize files based on year", required=False, callback=year)
@click.option("-p", "--path", type=str, help = "Path to organize", required=False, default=os.getcwd())
@click.pass_context
def main(ctx, type, all, keyword, year, path):
    """Welcome to Categorize!"""


