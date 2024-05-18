from aiogram import Bot
import os
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from dotenv import load_dotenv

load_dotenv()

PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')


async def order(msg: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali tolov!",
        description="Telegram bot orqali tolov qilishni organvommiz!",
        provider_token=PROVIDER_TOKEN,
        currency="sum",
        payload="Ichki malumot",
        prices=[
            LabeledPrice(label="skidka", amount=-2),
            LabeledPrice(label="Bonus", amount=-1)
        ]
    )

async def pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
