import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token
import random

token = token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет я загадал число от 1-3, попробуй его отгадать")

numbers = ("1", "2", "3")


@dp.message_handler(text=['1'])
async def start(message: types.Message):
    random_number = random.choice(numbers)
    if random_number == "1":
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text=['2'])
async def start(message: types.Message):
    random_number = random.choice(numbers)
    if random_number == "2":
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text=['3'])
async def start(message: types.Message):
    random_number = random.choice(numbers)
    if random_number == "3":
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(dp, skip_updates=True)