from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(text="Salom")
