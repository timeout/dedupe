import pytest
from dedupe.file_metadata import FileMetadata

class TestFileMetadataRepository:

    def test_create_file_metadata(self, repo, sample_metadata):
        result = repo.create(sample_metadata)

        assert result.id is not None

    def test_get_by_id(self, repo, sample_metadata):
        created = repo.create(sample_metadata)
        retrieved = repo.get_by_id(created.id)

        assert retrieved is not None
        assert retrieved.quick_hash == created.quick_hash

    def test_delete_by_id(self, repo, sample_metadata):
        created = repo.create(sample_metadata)
        retrieved = repo.get_by_id(created.id)

        assert retrieved.id is not None

        repo.delete(retrieved.id)

        assert repo.get_by_id(created.id) is None

    def test_get_all_duplicates(self, repo, sample_metadata, duplicate_metadata_group):
        unique = repo.create(sample_metadata)
        for duplicate_metadata in duplicate_metadata_group:
            repo.create(duplicate_metadata)

        created = repo.get_all()
        assert len(created) == 4

        duplicates = repo.get_all_duplicates()
        assert len(duplicates) == 1

        duplicate_quick_hash = duplicates[0]
        assert duplicate_quick_hash == "same_hash"

        assert unique.quick_hash not in duplicates
