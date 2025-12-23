from returns.io import impure_safe

from dedupe.repository.file_metadata_repository import FileMetadataRepository
from dedupe.file_metadata import FileMetadata


def save_to_db(repository: FileMetadataRepository):
    @impure_safe
    def _save(file_metadata: FileMetadata) -> FileMetadata:
        result = repository.create(file_metadata)

        if hasattr(result, 'unwrap'):
            metadata = result.unwrap()
        else:
            metadata = result

        print(f"Saved metadata: {metadata}")

        return metadata

    return _save
