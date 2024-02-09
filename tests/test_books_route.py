import json
from pathlib import Path

from api_vps.schemas.books import Books


def test_read_books():
    with open(Path(__file__).parent.parent / "static" / "books.json") as file:
        data = json.load(file)

    assert data == Books(data=data).model_dump()["data"]
