from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart

from keyboards import apple_kb, buy_ikb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=apple_kb)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    text = msg.web_app_data.data
    narxlari = 0

    products = text.split("|")
    for i in range(len(products)):
        if len(products[i]) >= 2:
            title = products[i].split('/')[0]
            price = float(products[i].split('/')[1])
            quantity = int(products[i].split('/')[2])

            await msg.answer(text=f"Nomi: {title}\n"
                                  f"Narxi: {price}\n"
                                  f"Soni: {quantity}\n"
                                  f"Umumiy narxi: {quantity * price}$")
            narxlari += price * quantity
    await msg.answer(text=f"Mahsulot uchun tolov qiling: {round(narxlari, 2)}$", reply_markup=buy_ikb)

