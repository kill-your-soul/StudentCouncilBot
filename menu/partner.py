from vkbottle.bot import Blueprint, Message
from vkbottle import Keyboard, Text, BaseStateGroup
from .utils.hello_keyboard import hello_keyboard, yes_or_not

bp = Blueprint()


class State(BaseStateGroup):
    STATE = 1
    q = 2


@bp.on.message(text="Партнер")
async def work(message: Message):
    keyboard = (
        Keyboard()
        .add(Text("Контакты Студенческого Совета"))
        .row()
        .add(Text("Предложение о сотрудничестве"))
        .row()
        .add(Text("Запрос публикации"))
    )
    await message.answer(
        "Приветствуем Вас в разделе Партнер. Мы заинтересованы в сотрудничестве, поэтому просим соблюдать алгоритм обращения, чтобы взаимодействие было продуктивным! Выбор раздела, который Вас интересует представлен ниже: ",
        keyboard=keyboard,
    )
    await bp.state_dispenser.set(message.peer_id, state=State.STATE)
    # await hello_keyboard(message, text="Продолжим")


@bp.on.message(text="Контакты Студенческого Совета", state=State.STATE)
async def contacts(message: Message):
    await message.answer(
        """Председатель — делегат от СПбГАСУ — @egorilina (Егор Ильин). 
Секретарь — делегат от НИУ ВШЭ — @rimiftakhutdinov (Руслан Мифтахутдинов)
Руководитель Медиа – делегат от СПбГЭТУ «ЛЭТИ» — @helen_guhman (Гухман Елена)
Руководитель внешнего взаимодействия - @chiefofthenorth (Куранову Леониду)
""",
        disable_mentions=False,
    )
    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, State.q)


@bp.on.message(text="Предложение о сотрудничестве", state=State.STATE)
async def collab(message: Message):
    await message.answer(
        """По вопросам сотрудничества писать на почту studsovetsaint-petersburg@yandex.ru
Соглашение о сотрудничестве необходимо предоставить на официальном бланке организации"""
    )
    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, State.q)


@bp.on.message(text="Запрос публикации", state=State.STATE)
async def publication(message: Message):
    await message.answer(
        """Запрос на публикацию необходимо отправить Руководителю внешнего взаимодействия - @chiefofthenorth (Куранову Леониду). Запрос на публикацию составляется по следующей форме:\n\n
- текст поста (содержание поста);
- картинка;
- срок публикации\n\n
Запрос рассматривается в течение 2 дней, после сообщим вам о нашем решении
"""
    )
    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, State.q)


@bp.on.message(text="Да", state=State.q)
async def yes(message: Message):
    await hello_keyboard(message, "Продолжаем")
    await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text="Нет", state=State.q)
async def no(message: Message):
    await message.answer('Спасибо за обращение. Чтобы начать снова напишите "Начать"')
    await bp.state_dispenser.delete(message.peer_id)
