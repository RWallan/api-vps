from enum import Enum

import httpx
from pydantic import JsonValue
from pydantic.dataclasses import dataclass


@dataclass
class HttpResponse:
    status_code: int
    json: JsonValue


class HttpMethods(Enum):
    post = "POST"
    get = "GET"
    put = "PUT"
    delete = "DEL"


class HttpRequester:
    def __init__(self, domain: str) -> None:
        self.__domain = domain
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
        self._client = httpx.AsyncClient(base_url=self.__domain)

        self.methods = {
            "post": self._client.post,
            "get": self._client.get,
            "put": self._client.put,
            "delete": self._client.delete,
        }
