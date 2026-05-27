from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# --- حقوق الملكية ---
# Developed by: L7MA9 SHOP
# --------------------

TOKEN = "ضع_التوكن_الجديد_هنا"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# القائمة الرئيسية
def get_main_menu():
    buttons = [
        [InlineKeyboardButton(text="💎 المنتجات", callback_data="products")],
        [InlineKeyboardButton(text="💳 طرق الدفع", callback_data="payments")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("أهلاً بك في متجر L7MA9 SHOP! اختر ما تحتاجه:\n\n--- L7MA9 SHOP ---", reply_markup=get_main_menu())

@dp.callback_query(F.data == "products")
async def show_products(callback: types.CallbackQuery):
    # هنا سيتم لاحقاً جلب المنتجات من قاعدة البيانات
    await callback.message.answer("لدينا حالياً: كود هاك (5 USDT)\nأرسل '1' لشراء كود واحد.")

@dp.message(F.text == "1")
async def process_buy(message: types.Message):
    # هنا يظهر رقم بايننس بعد تحديد الطلب
    await message.answer("السعر: 5 USDT\nيرجى الدفع لهذا الـ ID: `1077458202`\nثم أرسل رقم الطلب.\n\n--- L7MA9 SHOP ---")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
