from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
import asyncio

TOKEN = "8292008804:AAFXg7RzYfF4aBZiptA2o6GiU_IytzhG9PI"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

# Кнопка покупки
buy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💳 Купити курс",
                url="https://your-payment-link.com"
            )
        ]
    ]
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        """
🏋️ <b>Онлайн-курс зі спорту</b>

У цьому курсі ти дізнаєшся:

✅ Як правильно тренуватися
✅ Як скласти програму тренувань
✅ Основи правильного харчування
✅ Як досягати результатів без травм

Натисни кнопку нижче, щоб придбати курс.
""",
        reply_markup=buy_keyboard
    )


@dp.message(Command("paid"))
async def paid(message: Message):
    await message.answer(
        """
🏅 <b>Доступ відкрито!</b>

Спорт допомагає:
• зміцнити здоров'я
• розвинути витривалість
• покращити дисципліну

Дякуємо за покупку 💪
"""
    )


async def main():
    print("Бот запущено ✅")

    # очищає старі вебхуки
    await bot.delete_webhook(drop_pending_updates=True)

    # запуск
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())