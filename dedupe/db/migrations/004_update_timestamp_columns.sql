BEGIN TRANSACTION;

CREATE TABLE file_metadata_new (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	absolute_path TEXT NOT NULL,
	filename TEXT NOT NULL,
	size INTEGER NOT NULL,
	created_at REAL,
	mocified_at REAL,
	scanned_at REAL,
	quick_hash TEXT
);

INSERT INTO file_metadata_new (id, absolute_path, filename, size, created_at, quick_hash)
SELECT
	id,
	absolute_path,
	filename,
	size,
	CASE
		WHEN created_at IS NULL THEN NULL
		WHEN created_at LIKE '%-%-%T%:%:%' THEN strftime('%s', created_at)
		ELSE CAST(created_at AS REAL)
	END as created_at,
	quick_hash
FROM file_metadata;

DROP TABLE file_metadata;

ALTER TABLE file_metadata_new RENAME TO file_metadata;

COMMIT;
