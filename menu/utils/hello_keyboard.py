from vkbottle.bot import Message
from vkbottle import Keyboard, Text


async def hello_keyboard(message: Message, text) -> None:
    keyboard = (
        Keyboard(one_time=True, inline=False)
        .add(Text("Студент"))
        .row()
        .add(Text("Партнер"))
        .row()
        .add(Text("Организатор проекта/мероприятия"))
        .row()
        .add(Text("Основная информация"))
    ).get_json()
    await message.answer(text, keyboard=keyboard)


async def yes_or_not(message: Message) -> None:
    keyboard = Keyboard(one_time=True, inline=False).add(Text("Да")).add(Text("Нет"))
    await message.answer("Хотите продолжить?", keyboard=keyboard)
