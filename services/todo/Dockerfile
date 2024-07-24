FROM python:alpine3.20

RUN mkdir -p /app
WORKDIR /app

RUN apk add --no-cache bash
RUN apk add make
RUN apk add sqlite

COPY requirements.txt /app

ADD . /app

RUN make setup

EXPOSE 4001

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:4001", "app:server"]