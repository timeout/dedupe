__version__ = "0.1.0"

from dedupe.db.database import Database
from dedupe.file_metadata import FileMetadata
from dedupe.repository.file_metadata_repository import FileMetadataRepository

__all__ = ["Database", "FileMetadata", "FileMetadataRepository"]
