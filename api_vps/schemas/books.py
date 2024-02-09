from pydantic import BaseModel


class Book(BaseModel):
    titulo: str
    autor: str
    area: str
    imagem: str
    publisher: str
    ano_publicacao: int
    isbn: str


class Books(BaseModel):
    data: list[Book]
