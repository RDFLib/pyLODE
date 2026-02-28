import tomllib
from pathlib import Path

_pyproject_file = Path(__file__).parent.parent / "pyproject.toml"
with _pyproject_file.open("rb") as f:
    _data = tomllib.load(f)

__version__ = _data["project"]["version"]
