from fastapi import APIRouter

from api_vps import controllers, schemas

router = APIRouter(prefix="/api/books")


@router.get("/", response_model=schemas.Books)
async def get_books():
    book_controller = controllers.Books()
    books = await book_controller.read_books()

    return books
