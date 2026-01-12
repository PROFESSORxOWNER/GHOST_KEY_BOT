from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔑 Purchase Key")],
        [KeyboardButton(text="📄 My Keys"), KeyboardButton(text="🎁 Redeem Code")],
        [KeyboardButton(text="📘 How to Buy?")],
        [KeyboardButton(text="🆔 My ID"), KeyboardButton(text="🆘 Contact Support")]
    ],
    resize_keyboard=True
)

brands_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="VISION"), KeyboardButton(text="LETHAL")],
        [KeyboardButton(text="AORUS MOBILE"), KeyboardButton(text="CROZN ADMIN")],
        [KeyboardButton(text="CROZN CHEAT"), KeyboardButton(text="CROZN WALL HACK")],
        [KeyboardButton(text="⬅ Back")]
    ],
    resize_keyboard=True
)

duration_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="5 Hours – ₹25"), KeyboardButton(text="1 Day – ₹99")],
        [KeyboardButton(text="7 Days – ₹449"), KeyboardButton(text="30 Days – ₹799")],
        [KeyboardButton(text="60 Days – ₹899")],
        [KeyboardButton(text="⬅ Back to Brands")]
    ],
    resize_keyboard=True
)
