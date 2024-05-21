# import os
# from aiogram import Dispatcher, F, Bot
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
# from keyboards import apple_kb, buy_ikb
# from dotenv import load_dotenv
#
# load_dotenv()
# PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
#
# BOT_TOKEN = os.getenv("BOT_TOKEN")
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def start(msg: Message):
#     await msg.answer("Salom", reply_markup=apple_kb)
#
#
# @dp.message(Command("pay"))
# async def order(msg: Message):
#     await bot.send_invoice(
#         chat_id=msg.chat.id,
#         title="Telegram orqali tolov!",
#         description="Tolov qmasen erkemassa!",
#         provider_token=PROVIDER_TOKEN,
#         currency="UZS",
#         payload="Ichki malumot",
#         prices=[
#             LabeledPrice(label="skidka", amount=200000),
#             LabeledPrice(label="Bonus", amount=100000)
#         ]
#     )
#
#
# @dp.pre_checkout_query()
# async def pre_checkout(checkout_query: PreCheckoutQuery, bot: Bot):
#     await bot.answer_pre_checkout_query(checkout_query.id, ok=True)
#
#
# @dp.message(F.func(lambda msg: msg.web_app_data.data))
# async def get_btn(msg: Message):
#     text = msg.web_app_data.data
#     products_data = text.split("|")
#     products = {}
#     summa = 0
#     for i in range(len(products_data)):
#         if len(products_data[i].split("/")) >= 3:
#             title = products_data[i].split('/')[0]
#             price = float(products_data[i].split('/')[1])
#             quantity = int(products_data[i].split('/')[2])
#             product = {
#                 "Nomi": title,
#                 "Price": price,
#                 "Quantity": quantity
#             }
#             product.update(product)
#             await msg.answer(text=f"Nomi: {title}\n"
#                                   f"Narxi: {price}\n"
#                                   f"Soni: {quantity}\n"
#                                   f"Umumiy narxi: {quantity * price}$")
#             summa += price * quantity
#
#

import os
from aiogram import Dispatcher, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards import apple_kb, buy_ikb
from dotenv import load_dotenv

load_dotenv()
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

user_cart = {}


@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Salom", reply_markup=apple_kb)


@dp.message(Command("pay"))
async def order(msg: Message):
    user_id = msg.from_user.id
    if user_id not in user_cart:
        await msg.answer("Savatchangiz bo'sh!")
        return

    items = user_cart[user_id]
    prices = [LabeledPrice(label=item['title'], amount=item['price'] * 100) for item in items]

    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali tolov!",
        description="Tolov qmasn erkemassan!",
        provider_token=PROVIDER_TOKEN,
        currency="UZS",
        payload="Ichki malumot",
        prices=prices
    )


@dp.pre_checkout_query()
async def pre_checkout_query(checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(checkout_query.id, ok=True)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: Message):
    text = msg.web_app_data.data
    products = text.split("|")
    user_id = msg.from_user.id
    user_cart[user_id] = []

    for product in products:
        if len(product.split("/")) >= 3:
            title = product.split('/')[0]
            price = float(product.split('/')[1])
            quantity = int(product.split('/')[2])
            user_cart[user_id].append({
                'title': title,
                'price': price * quantity  # Store total price for each product
            })
            await msg.answer(
                text=f"Nomi: {title}\n"
                     f"Narxi: {price}\n"
                     f"Soni: {quantity}\n"
                     f"Umumiy narxi: {quantity * price} UZS"
            )

    summa = sum(item['price'] for item in user_cart[user_id])
    await msg.answer(text=f"Tolanishi kerak: {summa} UZS", reply_markup=buy_ikb)