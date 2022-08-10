import logging
from vkbottle.bot import Bot, Message
from menu.utils.hello_keyboard import hello_keyboard
from menu import bps
import os

bot = Bot(
    token=os.environ["TOKEN"]
)


@bot.on.message(text="Начать", state=None)
async def start(message: Message):
    await hello_keyboard(message, "Выберите раздел")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for bp in bps:
        bp.load(bot)
    bot.run_forever()
