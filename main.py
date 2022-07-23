import logging
from aiogram import Bot, Dispatcher, executor, types
from oxford import getDefinitions

API_TOKEN = '1486102810:AAFvHpYw-tXVtURdxy0XBR26rjkcaWiFJTk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🇬🇧 Enter the word:\n"
                         "🇷🇺 Вводите слово:\n"
                         "🇺🇿 So'z kiriting: ")


@dp.message_handler()
async def dict(message: types.Message):
    word_id = message.text
    lookup = getDefinitions(word_id)
    if lookup:
        await message.answer(f"Word: {word_id}\nDefinitions:\n{lookup['definitions']}")
        if lookup.get('audio'):
            await message.answer_audio(lookup['audio'])
    else:
        await message.reply("Sorry, no such word found!")


executor.start_polling(dp)
