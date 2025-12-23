from pathlib import Path
from typing import Iterator

def scan_directory(
    root: Path,
    pattern: str = "*",
    recursive: bool = True
) -> Iterator[Path]:
    if not root.is_dir():
        return

    glob_method = root.rglob if recursive else root.glob

    for path in glob_method(pattern):
        if path.is_file():
            yield path
