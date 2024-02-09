import pytest

from api_vps.utils.http_requester import HttpRequester, HttpResponse


@pytest.mark.asyncio
async def test_http_requester():
    http_requester = HttpRequester("https://jsonplaceholder.typicode.com")

    response = await http_requester.fetch("/todos/1", method="GET")

    assert response == HttpResponse(
        status_code=200,
        json={
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False,
        },
    )
