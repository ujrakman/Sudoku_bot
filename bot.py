import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ============ ВАШИ ДАННЫЕ ============
# Ваш токен от BotFather
TOKEN = "9234147362:AAESruP6pboN65qSHA3VEfKSZaxhcP_m41Q"

# Ссылка на вашу игру, которую вы загрузили на Tiiny.host
WEB_APP_URL = "https://index-2ce58f.tiiny.site" 
# ====================================

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Создаем кнопку, которая открывает Web App
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Играть в Судоку", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    
    text = (
        "Привет! Это игра Судоку.\n\n"
        "Нажми на кнопку ниже, чтобы открыть игровое поле. "
        "Там ты сможешь выбирать клетки и вводить цифры прямо внутри Telegram."
    )
    await message.answer(text, reply_markup=kb)

async def main():
    print("✅ Подключаюсь к Telegram...")
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Проверяем, что токен верный и бот существует
    me = await bot.get_me()
    print(f"✅ Бот @{me.username} запущен и готов к работе!")
    print("👉 Открой Telegram и напиши боту /start")
    
    # Запускаем бесконечный цикл получения сообщений
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())