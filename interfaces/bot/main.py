import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from services.user_service import UserService
from infrastructure.db.uow import UnitOfWork




API_TOKEN = os.getenv("TG_BOT_TOKEN")



bot = Bot(token=API_TOKEN)
dp = Dispatcher()
user_service = UserService(UnitOfWork)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_service.register_user(message.from_user.id, message.from_user.username)
    await message.answer("Ты зарегистрирован!")

@dp.message(Command("top"))
async def cmd_top(message: Message):
    users = user_service.get_top_users()
    text = "\n".join([f"{u.username or u.id} — {u.taps}" for u in users])
    await message.answer(f"Топ:\n{text}")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
