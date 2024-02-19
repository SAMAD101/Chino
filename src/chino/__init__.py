# __init__.py

from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

__version__ = "1.0.0"
