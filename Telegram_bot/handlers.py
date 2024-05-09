from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from Telegram_bot.keyboards import apple_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(text="Salom", reply_markup=apple_kb)

@dp.message(F.func(lambda msg: msg.web_app_data.data == "TestMessage"))
async def get_btn(msg: types.Message):
    print(msg)
    await msg.answer(msg.web_app_data.data)
