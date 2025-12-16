import pytest
import tempfile
import os

from dedupe.db import Database
from dedupe.repository.file_metadata_repository import FileMetadataRepository
from dedupe.file_metadata import FileMetadata


@pytest.fixture
def temp_db_path():
    temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".db")
    temp_file.close()
    db_path = temp_file.name

    yield db_path

    # clean up
    if os.path.exists(db_path):
        os.unlink(db_path)

@pytest.fixture
def temp_db(temp_db_path):
    db = Database(temp_db_path)
    db.run_migrations()

    yield db

    db.close()

@pytest.fixture
def repo(temp_db):
    return FileMetadataRepository(temp_db)

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


