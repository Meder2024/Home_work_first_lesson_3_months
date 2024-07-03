import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6503445658:AAEMwYLgd81_dXrBvoqqjTmFyilWXUSk5cM")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет")

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer("""
I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).

You can control me by sending these commands:

/newbot - create a new bot
/mybots - edit your bots

Edit Bots
/setname - change a bot's name
/setdescription - change bot description
/setabouttext - change bot about info
/setuserpic - change bot profile photo
/setcommands - change the list of commands
/deletebot - delete a bot""")


@dp.message_handler(text=['Салам', "салам", "salam"])
async def start(message: types.Message):
    await message.answer("Салам")

@dp.message_handler()
async def start(message: types.Message):
    await message.answer("Я вас не понял, нажмите на /help")

executor.start_polling(dp)