from aiogram import Router, F
from aiogram.types import Message

from db.models import Users
from db.repository import UsersRepository, users_repository
from utils.gpt_api import API_GPT

user_router = Router()


@user_router.message(F.text)
async  def get_question_to_ai(message: Message):
    question = message.text
    user_id = message.from_user.id
    username = message.from_user.username
    user = await users_repository.get_user_by_user_id(user_id=user_id)
    if user is None:
        user = await users_repository.add_user(user_id=user_id,username=username)
        await message.answer('hello')
        return
    thread_id = user.ai_thread_id
    answer = await API_GPT(thread_id).send_message(user_id=user_id, username=username, text=question, image_bytes= None)
    #print(answer)
    if answer is None:
        await message.answer('You not enter question')
    else:
        await message.answer(answer)
