from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

web_app = WebAppInfo(url="https://anvar0037.github.io/modul_11.github.io/")


apple_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Mini Up', web_app=web_app)]
], resize_keyboard=True)

buy_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Tolov", callback_data='buy')],
])
