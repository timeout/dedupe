from dataclasses import dataclass
from typing import Optional

@dataclass
class FileMetadata:
    id: Optional[int]
    absolute_path: str
    filename: str
    size: int
    quick_hash: Optional[str] = None
    created_at: Optional[str] = None

    @classmethod
    def from_row(cls, row):
        """Create file metadata from a database row"""
        return cls(
                id=row["id"],
                absolute_path=row["absolute_path"],
                filename=row["filename"],
                size=row["size"],
                quick_hash=row["quick_hash"],
                created_at=row["created_at"]
        )
