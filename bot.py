import asyncio

from aiogram import Bot, Dispatcher

from db.engine import DatabaseEngine
from handlerses.user_handlers import user_router
from settings import storage_bot

token = '7411913328:AAFr24UfkWUEGn_0sjcWSJIuhcgwYMeRggA'
main_bot = Bot(token=token)


async def main():
    db_engine = DatabaseEngine()
    await db_engine.proceed_schemas()
    print(await main_bot.get_me())
    dp = Dispatcher(storage=storage_bot)
    dp.include_routers(user_router)
    await dp.start_polling(main_bot)

asyncio.run(main())