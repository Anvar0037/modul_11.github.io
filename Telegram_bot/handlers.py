import os
from aiogram import Dispatcher, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from keyboards import apple_kb, buy_ikb
from dotenv import load_dotenv

load_dotenv()
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Salom", reply_markup=apple_kb)


@dp.message(Command("pay"))
async def order(msg: Message):
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali to'lov!",
        description="Telegram bot orqali to'lov qilishni o'rganyammiz!",
        provider_token=PROVIDER_TOKEN,
        currency="UZS",
        payload="Ichki malumot",
        prices=[
            LabeledPrice(label="skidka", amount=2),
            LabeledPrice(label="Bonus", amount=1)
        ]
    )


async def pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: Message):
    text = msg.web_app_data.data
    products = text.split("|")
    summa = 0
    for i in range(len(products)):
        if len(products[i].split("/")) >= 3:
            title = products[i].split('/')[0]
            price = int(products[i].split('/')[1])
            quantity = int(products[i].split('/')[2])
            await msg.answer(text=f"Nomi: {title}\n"
                                  f"Narxi: {price}\n"
                                  f"Soni: {quantity}\n"
                                  f"Umumiy narxi: {quantity * price}$")
            summa += price * quantity
    await msg.answer(text=f"To'lanishi kerak: {summa}$", reply_markup=buy_ikb)