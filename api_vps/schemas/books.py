from pydantic import BaseModel, HttpUrl


class Book(BaseModel):
    titulo: str
    autor: str
    area: str
    imagem: HttpUrl
    publisher: str
    ano_publicacao: int
    isbn: str


class Books(BaseModel):
    data: list[Book]
