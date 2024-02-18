import pytest

from chino.utils import *
from rich.console import Console


def test_fancy_print() -> None:
    console: Console = Console()
    fancy_print(console, "Hello, World!")
    fancy_print(console, "Hello, World!", isQuery=True)
    assert True
