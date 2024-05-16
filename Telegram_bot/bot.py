import os
import asyncio
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)


async def main():
    print('Bot started')
    from handlers import dp
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
