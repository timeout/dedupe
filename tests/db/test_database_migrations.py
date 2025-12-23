import pytest

import db.migration_queries as test_query


class TestDatabaseMigrations:
    """Test database initialization and migrations"""

    def test_database_created(self, temp_db):
        assert temp_db is not None
        assert temp_db.conn is not None

    def test_migrations_table_exists(self, temp_db):
        cursor = temp_db.execute(test_query.SELECT_SCHEMA_MIGRATIONS)
        assert cursor.fetchone() is not None

    def test_migrations_idempotent(self, temp_db):
        temp_db.run_migrations()
        temp_db.run_migrations()

        cursor = temp_db.execute(test_query.COUNT_SCHEMA_MIGRATIONS)
        result = cursor.fetchone()
        assert result["count"] > 0

    def test_migration_has_run(self, temp_db):
        cursor = temp_db.execute(test_query.SELECT_FIRST_SCHEMA_MIGRATION)
        row = cursor.fetchone()

        if row:
            version = row["version"]
            assert temp_db.has_migration_run(version) is True

        assert temp_db.has_migration_run("999_fake_migration") is not True


        
