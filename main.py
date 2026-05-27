import asyncio
from aiogram import Bot, Dispatcher
import handlers  # استدعاء ملف الأوامر والأزرار
import database  # استدعاء ملف القاعدة

# --- إعدادات البوت ---
TOKEN = "ضع_التوكن_هنا"
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    # 1. تهيئة قاعدة البيانات عند التشغيل
    database.init_db()
    
    # 2. تسجيل الـ Router الذي يحتوي على الأوامر
    dp.include_router(handlers.router)
    
    print("🚀 L7MA9 SHOP Bot is running successfully...")
    
    # 3. تشغيل البوت (Polling)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # تشغيل النظام كاملاً
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")

# L7MA9 SHOP - THE ULTIMATE STORE SYSTEM
# Completed Successfully.
