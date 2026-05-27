from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

# --- حقوق الملكية ---
# Bot Created by: L7MA9 SHOP
# Powered by Python & Aiogram

TOKEN = "ضع_التوكن_هنا"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً بك في L7MA9 SHOP!\nالمتجر تحت التطوير بواسطة L7MA9.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
