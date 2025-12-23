
CREATE = """
    INSERT INTO file_metadata (absolute_path, filename, size, quick_hash)
    values (?, ?, ?, ?)
"""

READ_ALL = """
    SELECT *
    FROM file_metadata
"""

READ_BY_ID = """
    SELECT *
    FROM file_metadata
    WHERE id = ?
"""

READ_BY_QUICK_HASH = """
    SELECT *
    FROM file_metadata
    WHERE quick_hash = ?
"""

READ_ALL_DUPLICATES = """
    SELECT quick_hash
    FROM file_metadata
    GROUP BY quick_hash
    HAVING COUNT(quick_hash) > 1
"""

DELETE_BY_ID = """
    DELETE FROM file_metadata
    WHERE id = ?
"""
