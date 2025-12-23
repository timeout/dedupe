import pytest

from dedupe.file_metadata import FileMetadata

@pytest.fixture
def sample_metadata():
    return FileMetadata(
        id=None,
        absolute_path="/test/path/file.jpg",
        filename="file.jpg",
        size=1024,
        quick_hash="hash123"
    )

@pytest.fixture
def sample_metadata_list():
    return [
        FileMetadata(
            id=None,
            absolute_path="/test/path/file1.jpg",
            filename="file1.jpg",
            size=1024,
            quick_hash="hash1"
        ),
        FileMetadata(
            id=None,
            absolute_path="/test/path/file2.jpg",
            filename="file2.jpg",
            size=1024,
            quick_hash="hash2"
        ),
        FileMetadata(
            id=None,
            absolute_path="/test/path/file3.jpg",
            filename="file3.jpg",
            size=1024,
            quick_hash="hash3"
        )
    ]

@pytest.fixture
def duplicate_metadata_group():
    return [
        FileMetadata(
            id=None,
            absolute_path="/test/path/file1.jpg",
            filename="file1.jpg",
            size=1024,
            quick_hash="same_hash"
        ),
        FileMetadata(
            id=None,
            absolute_path="/test/path/file2.jpg",
            filename="file2.jpg",
            size=1024,
            quick_hash="same_hash"
        ),
        FileMetadata(
            id=None,
            absolute_path="/test/path/file3.jpg",
            filename="file3.jpg",
            size=1024,
            quick_hash="same_hash"
        )
    ]


