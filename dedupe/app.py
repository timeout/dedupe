import logging
from dedupe.db.database import Database
from dedupe.file_metadata import FileMetadata
from dedupe.repository.file_metadata_repository import FileMetadataRepository

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

class App:
    def __init__(self, db_path="dedupe.db"):
        self.db = Database(db_path)
        self.db.run_migrations()

    def run(self):
        logger.info("Running app...")
        file_metadata = FileMetadata(
                id=None,
                absolute_path="/some/file/out/there.jpg",
                filename="there.jpg",
                size=1024,
                quick_hash="12345dead"
        )
        logger.info(f"Creating file metadata: {file_metadata}")

        repo = FileMetadataRepository(self.db)
        repo.create(file_metadata)

        duplicates = repo.get_all_duplicates()
        for duplicate in duplicates:
            logger.info(f"duplicate: {duplicate}")

        all_metadata = repo.get_all()
        for metadata in all_metadata:
            logger.info(metadata)
            repo.delete(metadata.id)

def main() -> None:
    app = App()
    app.run()
