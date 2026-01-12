import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from config import BOT_TOKEN
from keyboards import main_kb, brands_kb, duration_kb

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(msg: Message):
    await msg.answer(
        "🎮 Welcome to License Key Bot!\n\n"
        "24/7 ACTIVE & INSTANT KEY DELIVERY\n"
        "AUTO PAYMENT VERIFIED\n"
        "NO PAYMENT PROOF NEEDED",
        reply_markup=main_kb
    )

@dp.message(F.text == "🔑 Purchase Key")
async def purchase(msg: Message):
    await msg.answer("🎮 Select a brand to purchase:", reply_markup=brands_kb)

@dp.message(F.text.in_(["VISION","LETHAL","AORUS MOBILE","CROZN ADMIN","CROZN CHEAT","CROZN WALL HACK"]))
async def brand_selected(msg: Message):
    await msg.answer(f"⏳ Select duration for {msg.text}:", reply_markup=duration_kb)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
