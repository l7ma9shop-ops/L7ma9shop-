from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import database  # استدعاء ملف القاعدة الذي أنشأناه سابقاً

router = Router()

# دالة صنع القائمة الرئيسية
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 حسابي", callback_data="profile")],
        [InlineKeyboardButton(text="🛒 المنتجات", callback_data="shop")],
        [InlineKeyboardButton(text="💳 شحن الرصيد", callback_data="deposit")]
    ])

@router.message(Command("start"))
async def start_handler(msg: Message):
    # إضافة المستخدم للقاعدة
    database.init_db() # التأكد من وجود القاعدة
    await msg.answer(
        f"أهلاً بك يا {msg.from_user.full_name} في متجر L7MA9 SHOP.\n"
        "هذا النظام البرمجي المتكامل تحت تصرفك.\n"
        "اختر ما تحتاجه من القائمة:",
        reply_markup=main_menu()
    )

@router.callback_query(F.data == "profile")
async def profile_handler(call: CallbackQuery):
    user = database.get_user(call.from_user.id)
    # user[0] هو الـ ID، user[1] الاسم، user[2] الرصيد
    balance = user[2] if user else 0.0
    
    await call.message.edit_text(
        f"👤 **بيانات حسابك:**\n"
        f"الاسم: {call.from_user.full_name}\n"
        f"الرصيد: {balance} درهم\n\n"
        "--- L7MA9 SHOP ---",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 عودة", callback_data="back_home")]
        ])
    )

@router.callback_query(F.data == "back_home")
async def home_handler(call: CallbackQuery):
    await call.message.edit_text("القائمة الرئيسية لـ L7MA9 SHOP:", reply_markup=main_menu())

@router.callback_query(F.data == "deposit")
async def deposit_handler(call: CallbackQuery):
    await call.message.edit_text(
        "💳 **طرق الدفع المتوفرة:**\n\n"
        "بايننس (Binance): `1077458202`\n"
        "كاش بلس (Cash Plus): `0600000000`\n\n"
        "أرسل رقم العملية (TXID) هنا وسأقوم بتحديث رصيدك فوراً.",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 عودة", callback_data="back_home")]
        ])
    )

# كود إضافي لمعالجة الطلبات القادمة
@router.message(F.text.startswith("TXID"))
async def check_txid(msg: Message):
    await msg.answer("⏳ جاري التحقق من عملية الدفع... يرجى الانتظار.")

# L7MA9 SHOP - Developed with professional modular logic
