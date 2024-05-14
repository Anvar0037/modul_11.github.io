from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from Telegram_bot.keyboards import apple_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(text="Salom", reply_markup=apple_kb)

@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    text = msg.web_app_data.data
    print(text)
    title = text.split('/')[0]
    price = float(text.split('/')[1])
    quantity = int(text.split('/')[2])
    print(msg)
    await msg.answer(text=f"Nomi: {title} \n"
                          f"Soni: {quantity}\n"
                          f"Umumiy puli: {quantity * price}")
