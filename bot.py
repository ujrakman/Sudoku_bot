from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "9234147362:AAESruP6pboN65qSHA3VEfKSZaxhcP_m41Q"
WEB_APP_URL = "https://index-2ce58f.tiiny.site"

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Играть в Судоку", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    await message.answer("Привет! Нажми на кнопку ниже, чтобы открыть игру:", reply_markup=kb)
