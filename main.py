import os
import sqlite3
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# --- 1. الإعدادات ---
# ملاحظة: التوكن سنسحبه من الاستضافة ليكون آمناً (لا تضع التوكن هنا مباشرة)
TOKEN = os.environ.get("BOT_TOKEN") 
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- 2. قاعدة البيانات ---
def init_db():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, balance REAL DEFAULT 0.0)')
    conn.commit()
    conn.close()

# --- 3. الأزرار ---
def main_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 حسابي", callback_data="profile")],
        [InlineKeyboardButton(text="🛒 المنتجات", callback_data="shop")],
        [InlineKeyboardButton(text="💳 شحن الرصيد", callback_data="deposit")]
    ])

# --- 4. معالجة الأوامر ---
@dp.message(Command("start"))
async def start(msg: Message):
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (id, name, balance) VALUES (?, ?, ?)", (msg.from_user.id, msg.from_user.full_name, 0.0))
    conn.commit()
    conn.close()
    await msg.answer("مرحباً بك في L7MA9 SHOP!\nاختر ما تحتاجه:", reply_markup=main_kb())

@dp.callback_query(F.data == "profile")
async def profile(call: CallbackQuery):
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id = ?", (call.from_user.id,))
    bal = c.fetchone()[0]
    await call.message.edit_text(f"👤 المستخدم: {call.from_user.full_name}\n💰 رصيدك: {bal} درهم\n\n--- L7MA9 SHOP ---", reply_markup=main_kb())

@dp.callback_query(F.data == "deposit")
async def deposit(call: CallbackQuery):
    await call.message.edit_text("لشحن رصيدك أرسل المبلغ لبايننس:\n`1077458202`\nثم أرسل رقم العملية (TXID) هنا.", reply_markup=main_kb(), parse_mode="Markdown")

@dp.callback_query(F.data == "shop")
async def shop(call: CallbackQuery):
    await call.message.edit_text("المنتجات المتوفرة:\n1. كود هاك - 5$\nاختر للطلب.", reply_markup=main_kb())

# --- 5. التشغيل ---
async def main():
    init_db()
    print("Bot Started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
