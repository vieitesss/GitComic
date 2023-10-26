"""This program allows you to create a git commit including an icon"""

import re
import subprocess
from pathlib import Path
import typer
from typing_extensions import Annotated
from pyfzf.pyfzf import FzfPrompt
from rich import print as rprint

ICONS_FILE = (Path(__file__).parent / "../../assets/icons.txt").resolve()

fzf = FzfPrompt()
app = typer.Typer()


def choose_icon():
    """Reads the file with the icons and each description and returns the icons selected"""
    options = []
    with ICONS_FILE.open() as file:
        for line in file:
            options.append(line.strip())

    [opt] = fzf.prompt(options)

    [icon] = re.findall(r"(.*)[A-Z]", opt)
    return icon


@app.command()
def create_commit(message: Annotated[str, typer.Argument()]):
    """Creates a commit message with an icon"""
    icon = choose_icon()
    commit_message = f"{icon}{message}"
    output = subprocess.run(
        f'git commit -m "{commit_message}"', shell=True, check=False, capture_output=True
    ).stdout.decode()
    rprint(output)


if __name__ == "__main__":
    app()
