import logging
from . import universities, mail


async def send_email(university: str, text: str, theme: str):
    logging.info(university)
    if not university:
        reciever_email = "studsovetspb@gmail.com"

    else:
        reciever_email = next(
            item for item in universities if item["university"] == university
        )["email"]

    
    
    await mail.send_message(
        theme, to=reciever_email, from_address="spbss.info@gmail.com", body=text
    )
