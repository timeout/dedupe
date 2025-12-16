SELECT_SCHEMA_MIGRATIONS = """
    SELECT name
    FROM sqlite_master
    WHERE type='table' AND name="schema_migrations"
"""

COUNT_SCHEMA_MIGRATIONS = """
    SELECT COUNT(*) AS count
    FROM schema_migrations
"""

SELECT_FIRST_SCHEMA_MIGRATION = """
    SELECT version
    FROM schema_migrations
    LIMIT 1
"""
