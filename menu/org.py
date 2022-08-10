from vkbottle.bot import Blueprint, Message
from vkbottle import Keyboard, Text, BaseStateGroup
from .utils.hello_keyboard import hello_keyboard, yes_or_not

bp = Blueprint()


class question(BaseStateGroup):
    q = 1


@bp.on.message(text="Организатор проекта/мероприятия")
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
        "Приветствуем Вас в разделе организатор проекта/мероприятия. Мы заинтерисованы в сотрудничестве, поэтому просим соблюдать правила обращения, чтобы взаимодействие было продуктивным! Выберите раздел:",
        keyboard=keyboard,
    )
    # await hello_keyboard(message, text="Продолжим")


@bp.on.message(text="Контакты Студенческого Совета")
async def contacts(message: Message):
    await message.answer(
        """Председатель — делегат от СПбГАСУ — @egorilina (Егор Ильин). 
Секретарь — делегат от НИУ ВШЭ — @rimiftakhutdinov (Руслан Мифтахутдинов)
Руководитель Медиа – делегат от СПбГЭТУ «ЛЭТИ» — @helen_guhman (Гухман Елена)
Руководитель внешнего взаимодействия - @chiefofthenorth (Куранову Леониду)
""",
        disable_mentions=False,
    )
    await bp.state_dispenser.set(message.peer_id, state=question.q)
    await yes_or_not(message)


@bp.on.message(text="Предложение о сотрудничестве")
async def collab(message: Message):
    await message.answer(
        """По вопросам сотрудничества писать на почту studsovetsaint-petersburg@yandex.ru
Соглашение о сотрудничестве необходимо предоставить на официальном бланке организации"""
    )
    await bp.state_dispenser.set(message.peer_id, state=question.q)
    await yes_or_not(message)


@bp.on.message(text="Запрос публикации")
async def publication(message: Message):
    await message.answer(
        """Запрос на публикацию необходимо отправить Руководителю внешнего взаимодействия - @chiefofthenorth (Куранову Леониду). Запрос на публикацию составляется по следующей форме:\n\n
- текст поста (содержание поста);
- картинка;
- срок публикации\n\n
Запрос рассматривается в течение 2 дней, после сообщим вам о нашем решении
"""
    )
    await bp.state_dispenser.set(message.peer_id, state=question.q)
    await yes_or_not(message)


@bp.on.message(text="Да", state=question.q)
async def yes(message: Message):
    await hello_keyboard(message, "Продолжаем")
    await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text="Нет", state=question.q)
async def no(message: Message):
    await message.answer('Спасибо за обращение. Чтобы начать снова напишите "Начать"')
    await bp.state_dispenser.delete(message.peer_id)
