from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

from Telegram_bot.keyboards import apple_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(text="Salom", reply_markup=apple_kb)
