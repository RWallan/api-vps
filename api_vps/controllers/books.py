from fastapi import HTTPException

from api_vps import schemas
from api_vps.utils.http_requester import HttpMethods, HttpRequester


class Books:
    __domain: str = "https://books-api-practice.s3.sa-east-1.amazonaws.com"
    requester: HttpRequester

    def __init__(self):
        self.requester = HttpRequester(self.__domain)

    async def read_books(self) -> schemas.Books:
        response = await self.requester.fetch(
            "/books.json", method=HttpMethods.get
        )

        if response.status_code == 200:
            data = response.json
            return schemas.Books(data=data)

        raise HTTPException(
            status_code=response.status_code, detail=response.json
        )
