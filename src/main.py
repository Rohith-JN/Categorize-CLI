import os
import click


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
            mod = __import__(f"src.commands.{name}", None, None, ["main"])
        except ImportError:
            return
        return mod.main


@click.command(cls=ComplexCLI)
def main():
    """Welcome to Categorize!"""
    pass