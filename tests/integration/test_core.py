import pytest
from returns.result import Success, Failure
from returns.io import IOSuccess, IOFailure
from returns.pipeline import flow

from dedupe.steps.path_to_metadata import path_to_metadata, path_to_metadata_with_quick_hash
from dedupe.steps.hashers import quick_hash
from dedupe.steps.save_to_db import save_to_db 
from dedupe.scanner import scan_directory
from dedupe.file_metadata import FileMetadata

class TestCoreIntegration:

    def test_scan_and_save_file_metadata(self, temp_files, repo):
        save = save_to_db(repo)

        paths = scan_directory(temp_files)

        saved_count = 0
        for path in paths:
            result = path_to_metadata(path)

            if isinstance(result, Success):
                metadata = result.unwrap()
                save(metadata)
                saved_count += 1

        assert saved_count > 0

        all_files = repo.get_all()
        assert saved_count == len(all_files)
        
        filenames = [f.filename for f in all_files]
        assert "image1.jpg" in filenames

    def test_quick_scan_duplicate_detection(self, temp_files, repo):
        save = save_to_db(repo)

        paths = scan_directory(temp_files)

        saved_count = 0
        for path in paths:
            result = flow(
                path,
                path_to_metadata_with_quick_hash,
                lambda r: r.bind(save)
            )

            match result:
                case IOSuccess(success):
                    saved_count += 1
                    metadata = success.unwrap()
                    print(f"Saved {metadata.filename}")
                case IOFailure(error):
                    print(f"Failed: {error}")

        assert saved_count > 0
        print(f"saved: {saved_count}")

        all_files = repo.get_all()
        print(f"retrieved {len(all_files)} files")
        for file in all_files:
            print(f"metadata: {file.id}, {file.quick_hash}")
        duplicates = repo.get_all_duplicates()
        assert 1 == len(duplicates)

