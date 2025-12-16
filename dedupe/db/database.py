import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_migrations_table()

    def _init_migrations_table(self):
        """Create a table to track which migrations have run"""
        self.conn.execute(
                """CREATE TABLE IF NOT EXISTS schema_migrations (
                    version TEXT PRIMARY KEY,
                    applied_at TEXT DEFAULT CURRENT_TIMESTAMP
                )"""
        )
        self.conn.commit()

    def has_migration_run(self, version: str) -> bool:
        cursor = self.conn.execute(
                "SELECT 1 FROM schema_migrations WHERE version = ?",
                (version,)
        )
        return cursor.fetchone() is not None

    def record_migration(self, version: str) -> None:
        self.conn.execute(
                "INSERT INTO schema_migrations (version) VALUES (?)",
                (version,)
        )
        self.conn.commit()
        logger.info(f"Recorded migration {version}")

    def run_migrations(self, migrations_dir: str = "dedupe/db/migrations"):
        """Run all pending migrations in order"""
        migrations_path = Path(migrations_dir)
        logger.info(f"Running migratiions from directory {migrations_dir}")
        if not migrations_path.exists():
            logger.warn("Migrations directory not found!")
            return

        migration_files = sorted(migrations_path.glob("*.sql"))
        for migration_file in migration_files:
            version = migration_file.stem

            if self.has_migration_run(version):
                logger.info(f"Migration '{version}' has alrady run - skipping")
                continue

            logger.info(f"Running migration '{version}'")
            sql = migration_file.read_text()
            try:
                self.conn.executescript(sql)
                self.record_migration(version)
                logger.info(f"Migration '{version}' conpleted")
            except sqlite3.Error as e:
                logger.error(f"Migration '{version}' failed: {e}")
                raise

    def execute(self, sql: str, params: tuple = ()):
        """Execute an SQL query"""
        return self.conn.execute(sql, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
