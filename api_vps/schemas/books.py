from pydantic import BaseModel, HttpUrl


class Books(BaseModel):
    titulo: str
    autor: str
    area: str
    imagem: HttpUrl
    publisher: str
    ano_publicacao: int
    isbn: str
