import logging
from dedupe.db.database import Database

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

class App:
    def __init__(self, db_path="dedupe.db"):
        self.db = Database(db_path)
        self.db.run_migrations()

    def run(self):
        logger.info("Running app...")

def main() -> None:
    app = App()
    app.run()
