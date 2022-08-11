FROM python:3.10-alpine

WORKDIR /bot
RUN apk add musl-dev
RUN apk add --update gcc

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY static/ /bot/static
COPY main.py .
COPY menu/ /bot/menu
CMD [ "python", "main.py" ]