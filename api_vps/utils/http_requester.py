from enum import Enum
from typing import Any

import httpx
from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


@dataclass
class HttpResponse:
    status_code: int
    json: dict[str, Any]


class HttpMethods(Enum):
    post = "POST"
    get = "GET"
    put = "PUT"
    delete = "DEL"


class HttpRequester:
    def __init__(self, domain: HttpUrl) -> None:
        self.domain = domain
        self.__create_async_methods()

    async def fetch(
        self, endpoint: str, method: HttpMethods, **kwargs
    ) -> HttpResponse:
        response = await self.methods[HttpMethods(method).name](
            endpoint, **kwargs
        )

        return HttpResponse(
            status_code=response.status_code, json=response.json()
        )

    def __create_async_methods(self):
        self._client = httpx.AsyncClient(base_url=self.domain)

        self.methods = {
            "post": self._client.post,
            "get": self._client.get,
            "put": self._client.put,
            "delete": self._client.delete,
        }
