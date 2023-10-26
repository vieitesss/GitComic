#!./.venv/bin/python

"""This program allows you to create a git commit including an icon"""

import re
import subprocess
import typer
from typing_extensions import Annotated
from pyfzf.pyfzf import FzfPrompt
from rich import print as rprint

fzf = FzfPrompt()
app = typer.Typer()


def choose_icon():
    """Reads the file with the icons and each description and returns the icons selected"""
    options = []
    with open("icons.txt", encoding="utf-8") as file:
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
    rprint(f"[bold]Your commit message -> {commit_message}")
    subprocess.run(f"git commit -m {commit_message}", shell=True, check=True)


if __name__ == "__main__":
    app()
