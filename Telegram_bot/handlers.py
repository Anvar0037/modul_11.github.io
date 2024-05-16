from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from Telegram_bot.keyboards import apple_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=apple_kb)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    text = msg.web_app_data.data
    products = text.split("|")
    for i in range(len(products)):
        title = products[i].split('/')[1]
        price = int(products[i].split('/')[1])
        quantity = int(products[i].split('/')[2])
        await msg.answer(text=f"Mahsulot Nomi: {title}\n"
                              f"Mahsulot Narxi: {price}\n"
                              f"Mahsulot Soni: {quantity}\n"
                              f"Umumiy narxi: {quantity * price}$")



