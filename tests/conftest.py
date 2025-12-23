import pytest
import tempfile
import os

from dedupe.db import Database
from dedupe.repository.file_metadata_repository import FileMetadataRepository


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

