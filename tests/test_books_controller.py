import pytest

from api_vps.controllers.books import Books


@pytest.mark.asyncio
async def test_read_books():
    books = await Books().read_books()
    response = books.model_dump()

    assert len(response.get("data")) > 0
    assert "titulo" in response["data"][0]
    assert "autor" in response["data"][0]
    assert "area" in response["data"][0]
    assert "imagem" in response["data"][0]
    assert "publisher" in response["data"][0]
    assert "ano_publicacao" in response["data"][0]
    assert "isbn" in response["data"][0]
