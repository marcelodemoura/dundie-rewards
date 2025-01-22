import pkg_resources
import rich_click as click
from rich.table import Table
from rich.console import Console

from dundie import core 

@click.group
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """ Dundie Mifflin Rewards System.
    This CLI application DM rewards.
    """

@main.command()
@click.Argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database
    ## Features

    -
    """
    result = core.load(filepath)
    header = ["name","dept", "role", "e-mail"]
    for person in result:
        print("-" * 50)
        for key, value in zip(header, person.split(",")):
            print(f"{key} -> {value.strip()}")
