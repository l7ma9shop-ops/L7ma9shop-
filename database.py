import sqlite3

# L7MA9 SHOP - DATABASE ENGINE
# هذا الملف يحتوي على كل المنطق الخاص بحفظ البيانات

def init_db():
    """تهيئة الجداول الأساسية للمتجر"""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    # جدول المستخدمين: حفظ المعرف، الاسم، والرصيد
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        balance REAL DEFAULT 0.0
                    )''')
    
    # جدول المنتجات: حفظ السلع، أسعارها، والكمية المتوفرة
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        price REAL, 
                        stock INTEGER
                    )''')
    
    # جدول السجلات: لضمان عدم ضياع أي عملية دفع
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        user_id INTEGER, 
                        amount REAL, 
                        status TEXT
                    )''')
    
    conn.commit()
    conn.close()

def get_user(user_id):
    """جلب بيانات المستخدم من القاعدة"""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_balance(user_id, amount):
    """تحديث رصيد المستخدم بعد الشحن"""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
    conn.commit()
    conn.close()

# دالة لإضافة منتج جديد (تستخدمها أنت كأدمن)
def add_product(name, price, stock):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()

# إضافة تعليق برمجي للحماية
# L7MA9 SHOP - All rights reserved
