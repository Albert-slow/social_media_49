from fastapi import APIRouter, Request
from database.postservice import *

comment_router = APIRouter(prefix="/comment", tags=["Управление комментариями"])


@comment_router.post("/api/add_comment")
async def add_comment(user_id: int, post_id: int, text: str):
    new_comment = public_comment_db(user_id=user_id, post_id=post_id, text=text)
    if new_comment:
        return {"status": 1, "message": "Комментарий успешно добавлен"}
    return {"status": 0, "message": "Комментарий добавить не удалось"}


@comment_router.get("/api/get_comment")
async def get_exact_post_comments(post_id: int):
    comments = get_exact_post_comment_db(post_id)
    if comments:
        return {"status": 1, "message": comments}
    return {"status": 0, "message": "Комментарий не найден"}


@comment_router.put("/api/edit_comment")
async def change_post_comment(comment_id: int, new_text: str):
    if comment_id and new_text:
        change_comment_text_db(comment_id=comment_id, new_text=new_text)
        return {"status": 1, "message": "Комментарий успешно изменён"}
    return {"status": 0, "message": "Ошибка"}


@comment_router.delete("/api/delete_comment")
async def delete_post_comment(comment_id: int):
    try:
        delete_exact_comment_db(comment_id)
        return {"status": 1, "message": "Комментарий успешно удалён"}
    except:
        return {"status": 0, "message": "Не удалось удалить комментарий"}
