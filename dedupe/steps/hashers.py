import hashlib
from pathlib import Path
from returns.result import safe

from dedupe.file_metadata import FileMetadata

@safe
def quick_hash(path: Path, sample_size = 8192) -> str:
    md5_hasher = hashlib.md5()

    with open(path, 'rb') as f:
        chunk = f.read(sample_size)
        md5_hasher.update(chunk)

    digest = md5_hasher.hexdigest()
    return digest
