import pytest
import tempfile
import os
from pathlib import Path


@pytest.fixture
def temp_files(tmp_path):
    # unique files
    (tmp_path / "image1.jpg").write_bytes(b"x" * 1024)
    (tmp_path / "image2.jpg").write_bytes(b"x" * 2048)
    (tmp_path / "image3.jpg").write_bytes(b"x" * 4096)

    # duplicate files
    duplicate_content = b"duplicate content here"
    (tmp_path / "duplicate1.jpg").write_bytes(duplicate_content)
    (tmp_path / "duplicate2.jpg").write_bytes(duplicate_content)

    # sub-directory
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()

    (sub_dir / "image4.jpg").write_bytes(b"x" * 8192)

    # another duplicate
    (sub_dir / "another_duplicate1.jpg").write_bytes(duplicate_content)

    return tmp_path
