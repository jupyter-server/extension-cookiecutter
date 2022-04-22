#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_path(path: str) -> None:
    """Remove the provided path.

    If the target path is a directory, remove it recursively.
    """
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        for f in path.iterdir():
            remove_path(f)
        path.rmdir()


if __name__ == "__main__":

    if not "{{ cookiecutter.has_binder }}".lower().startswith("y"):
        remove_path(PROJECT_DIRECTORY / "binder")
        remove_path(PROJECT_DIRECTORY / ".github/workflows/binder-on-pr.yml")
