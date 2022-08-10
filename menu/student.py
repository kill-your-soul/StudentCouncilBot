import logging
from vkbottle.bot import Blueprint, Message
from vkbottle import BaseStateGroup, Keyboard, Text, EMPTY_KEYBOARD
from fuzzywuzzy import process

from menu.utils.hello_keyboard import hello_keyboard, yes_or_not
from .utils import unis
from .utils.rules import UniversityRule
from .utils.send_email import send_email


bp = Blueprint()


class StudentState(BaseStateGroup):
    FIRST_QUESTION = 1
    SECOND_QUESION = 2
    THIRD_QUESTION = 3
    FOURTH_QUESTION = 4
    FIFTH_QUESTION = 5


class OtherState(BaseStateGroup):
    QUESTION = 1


@bp.on.message(text="Студент", state=None)
async def student(message: Message):
    keyboard = (
        Keyboard().add(Text("У меня возникла проблема")).row().add(Text("Другое"))
    )
    await message.answer(
        "Привет, студент! У тебя есть уникальная возможность обратиться с проблемой или узнать основную информацию о нашей деятельности. Итак, начнем!",
        keyboard=keyboard,
    )
    await bp.state_dispenser.set(message.peer_id, StudentState.FIRST_QUESTION)


@bp.on.message(text="Другое", state=StudentState.FIRST_QUESTION)
async def other(message: Message):
    keyboard = (
        Keyboard()
        .add(Text("Контакты Студенческого совета"))
        .row()
        .add(Text("Информация о СС Спб"))
        .row()
        .add(Text("Памятка первокурсника"))
    )
    await message.answer(
        "В данном разделе ты можешь ознакомится с информацией о деятельности Студенческого совета Санкт-Петербурга, изучить памятку первокурссника, а также получить информацию об органах студенческого самоуправления нашего города. Выбор за тобой!",
        keyboard=keyboard,
    )
    await bp.state_dispenser.delete(message.peer_id)
    await bp.state_dispenser.set(message.peer_id, OtherState.QUESTION)


@bp.on.message(text="Контакты Студенческого совета", state=OtherState.QUESTION)
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
    await bp.state_dispenser.set(message.peer_id, state=StudentState.FIFTH_QUESTION)


@bp.on.message(text="Информация о СС Спб", state=OtherState.QUESTION)
async def info(message: Message):
    await message.answer(
        """Наш Совет начал свою работу на основании распоряжения Губернатора Санкт-Петербурга ещё в 1998 году. 
Сегодня Студенческий совет Санкт-Петербурга осуществляет свою деятельность на основании положения, утвержденного постановлением Правительства Санкт-Петербурга.

Студенческий совет Санкт-Петербурга является коллегиальным совещательным органом при Правительстве Санкт-Петербурга. 
Основными целями деятельности Студенческого совета являются:
— выработка предложений по реализации государственной молодежной политики в Санкт-Петербурге;
— выработка предложений по вопросам улучшения качества образовательного процесса;
— выработка предложений по повышению уровня подготовки специалистов, необходимых для эффективного социально-экономического развития Санкт-Петербурга;
— пропаганда и популяризация профессионального образования среди молодежи Санкт-Петербурга и др.

Ссылка на поставновление Правительства Санкт-Петербурга: https://docs.cntd.ru/document/8418051
""",
        dont_parse_links=True,
    )

    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, state=StudentState.FIFTH_QUESTION)


@bp.on.message(text="Памятка первокурсника", state=OtherState.QUESTION)
async def memo(message: Message):
    await message.answer(
        """Дорогой первокурсник! Мы от всей души поздравляем тебя с началом учебного года и желаем успехов во всех твоих начинаниях!
Для того, чтобы первые дни твоего студенчества были наполнены только позитивными моментами, мы предлагаем to-do лист для первокурсников:

1. Не забудь оформить студенческую БСК — бесконтакнтную смарт-карту! Используя БСК, ты сможешь существенно сэкономить на оплате проезда в общественном транспорте; выбирать проезд на всех видах транспорта или только на метро. Более подробную информацию об оформлении БСК ты можешь узнать в своём университете или на сайте: http://карта-онлайн.рф
2. Обязательно проверь, действует ли твой полис обязательного медицинского страхования, так как именно он будет твоим гарантом для получения бесплатной медицинской помощи в больнице или поликлинике. Если твой полис недействителен, то ты всегда можешь оформить новый. На время его изготовления тебе выдадут временное удостоверение, по которому ты в любой момент сможешь обратиться в медицинское учреждение.
3. Если ты — иногородний студент, то позаботься о получении временной регистрации! Как правило, те студенты, которые живут в общежитиях, автоматически ставятся на учет. Если же ты снимаешь жилье, то помни, что каждый гражданин России, который живет не по месту регистрации в течение более чем трех месяцев, должен получить временную регистрацию. Сделать это можно в паспортном столе или в многофункциональном центре.
4. Есть ещё один важный пункт, и он касается юношей — речь идет о постановке на воинский учёт. В каждой образовательной организации есть воинско-учётный стол, куда обязательно нужно прийти в начале года и предоставить все необходимые документы. После этого сотрудники учётного стола помогут тебе с предоставлением отсрочки от службы в армии.

Если у тебя остались вопросы, то ты смело можешь обратиться к нам или к ребятам, которые представляют интересы студентов в твоей образовательной организации.

Твой, Студсовет Санкт-Петербурга
""",
        dont_parse_links=True,
    )
    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, state=StudentState.FIFTH_QUESTION)


@bp.on.message(text="У меня возникла проблема", state=StudentState.FIRST_QUESTION)
async def problem(message: Message):
    keyboard = (
        Keyboard()
        .add(Text("Проблема связана с ОО"))
        .row()
        .add(Text("Проблема не связана с ОО"))
    )
    await message.answer(
        "Проблема, с которой ты столкнулся, может быть связана с твоей образовательной организацией или же связана с городом. Мы обязательно ответим и вернемся с решением!",
        keyboard=keyboard,
    )
    await bp.state_dispenser.set(message.peer_id, state=StudentState.SECOND_QUESION)


@bp.on.message(text="Проблема связана с ОО", state=StudentState.SECOND_QUESION)
async def organisation(message: Message):
    await message.answer("Введите аббревиатуру вашей образовательной организации", keyboard=EMPTY_KEYBOARD)
    await bp.state_dispenser.set(message.peer_id, state=StudentState.THIRD_QUESTION)


@bp.on.message(text="Проблема не связана с ОО", state=StudentState.SECOND_QUESION)
@bp.on.message(UniversityRule(), state=StudentState.THIRD_QUESTION)
async def essence(message: Message):
    await message.answer(
        f"Опишите основную суть проблемы",
        keyboard=EMPTY_KEYBOARD,
    )
    await bp.state_dispenser.set(
        message.peer_id, StudentState.FOURTH_QUESTION, payload=message.text
    )

@bp.on.message(state=StudentState.THIRD_QUESTION)
async def wrong_university(message: Message):
    await message.answer("Вы ввели неверную аббревиатуру вуза. Попробуйте еще раз")



@bp.on.message(state=StudentState.FOURTH_QUESTION)
async def problem_handler(message: Message):

    if message.state_peer.payload["payload"] == "Проблема не связанная с вузом":
        await message.answer(
            "Ваше сообщение вскоре будет отправлено на почту Председателя Студенческого совета Санкт-Петербурга"
        )
        await send_email(
            None,
            message.text,
            # message.state_peer.payload["payload"]
            "Обращение бота СС СПб",
        )
    else:
        await message.answer(
            "Ваше сообщение вскоре будет отправлено на почту председателя Студенческого совета вашей образовательной организации"
        )
        logging.info(message.client_info)
        await send_email(
            process.extractOne(message.state_peer.payload["payload"].lower(), unis)[0],
            message.text,
            # message.state_peer.payload["payload"],
            "Обращение бота СС СПб",
        )
    await bp.state_dispenser.delete(message.peer_id)
    await yes_or_not(message)
    await bp.state_dispenser.set(message.peer_id, state=StudentState.FIFTH_QUESTION)


@bp.on.message(text="Да", state=StudentState.FIFTH_QUESTION)
async def yes(message: Message):
    await hello_keyboard(message, "Продолжаем")
    await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text="Нет", state=StudentState.FIFTH_QUESTION)
async def no(message: Message):
    await message.answer('Спасибо за обращение. Чтобы начать снова напишите "Начать"')
    await bp.state_dispenser.delete(message.peer_id)
