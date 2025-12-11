from typing import List
from dedupe.db.database import Database
from dedupe.file_metadata import FileMetadata

class FileMetadataRepository:
    def __init__(self, db: Database):
        self.db = db

    def create(self, file_metadata: FileMetadata) -> FileMetadata:
        cursor = self.db.execute(
                "INSERT INTO file_metadata (absolute_path, filename, size, quick_hash) values (?, ?, ?, ?)",
                (file_metadata.absolute_path, file_metadata.filename, file_metadata.size, file_metadata.quick_hash)
        )
        self.db.commit()
        file_metadata.id = cursor.lastrowid

        return file_metadata

    def get_all(self) -> List[FileMetadata]:
        pass

    def update(self, fileMetadata: FileMetadata) -> FileMetadata:
        pass

    def delete(self, id: int):
        pass
