import dedupe.repository.file_metadata_queries as queries
from typing import List
from dedupe.db.database import Database
from dedupe.file_metadata import FileMetadata

class FileMetadataRepository:
    def __init__(self, db: Database):
        self.db = db

    def create(self, file_metadata: FileMetadata) -> FileMetadata:
        cursor = self.db.execute(
                queries.CREATE,
                (file_metadata.absolute_path, file_metadata.filename, file_metadata.size, file_metadata.quick_hash)
        )
        self.db.commit()
        file_metadata.id = cursor.lastrowid

        return file_metadata

    def get_all(self) -> List[FileMetadata]:
        cursor = self.db.execute(queries.READ_ALL)
        return [FileMetadata.from_row(row) for row in cursor.fetchall()]

    def get_all_duplicates(self) -> List[str]:
        cursor = self.db.execute(queries.READ_ALL_DUPLICATES)
        return [item[0] for item in cursor.fetchall()]

    def update(self, fileMetadata: FileMetadata) -> FileMetadata:
        pass

    def delete(self, file_metadata_id: int):
        self.db.execute(
                queries.DELETE_BY_ID,
                (file_metadata_id,)
        )
        self.db.commit()
