from pathlib import Path
import json

CONFIG_PATH = Path("config/config.json")


def load_config () -> dict:
    with CONFIG_PATH.open(
        mode="r",
        encoding="utf-8"
    ) as file:
        return json.load(file)
