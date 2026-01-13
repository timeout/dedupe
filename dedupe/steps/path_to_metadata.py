from pathlib import Path
from returns.result import Result, safe

from dedupe.file_metadata import FileMetadata
from dedupe.steps.hashers import quick_hash


@safe
def path_to_metadata(path: Path) -> FileMetadata:
    stat = path.stat()
    
    return FileMetadata(
        id=None,
        absolute_path=str(path.absolute()),
        filename=path.name,
        size=stat.st_size,
        created_at=stat.st_ctime
    )

def path_to_metadata_with_quick_hash(path: Path) -> FileMetadata:
    metadata_result = path_to_metadata(path)
    hash_result = quick_hash(path)

    return metadata_result.bind(
        lambda metadata: hash_result.map(
            lambda hash_val: FileMetadata(
                id=metadata.id,
                absolute_path=metadata.absolute_path,
                filename=metadata.filename,
                size=metadata.size,
                quick_hash=hash_val,
                created_at=metadata.created_at
            )
        )
    )
