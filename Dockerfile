FROM python:3.10-slim

WORKDIR /bot
# RUN apk add musl-dev mc-lang
# RUN export LANG=ru_RU.UTF-8
RUN apt-get update
RUN apt-get install -y gcc

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY static/ /bot/static
COPY main.py .
COPY menu/ /bot/menu
CMD [ "python", "main.py" ]