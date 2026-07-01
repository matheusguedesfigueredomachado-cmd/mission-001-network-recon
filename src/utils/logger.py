import logging
from pathlib import Path

LOG_FILE = Path("logs/application.log")

def setup_logger() -> None:
    LOG_FILE.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )