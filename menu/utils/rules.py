from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule
from fuzzywuzzy import process
from . import unis


class UniversityRule(ABCRule[Message]):
    async def check(self, event: Message) -> bool:
        procent = process.extractOne(event.text.lower(), unis)
        # print(procent)
        if procent[1] > 75:
            return True
