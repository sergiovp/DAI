FROM python:3

ENV PYTHONUNBUFFERED=1

# Al igual que en flask, nuestro directorio de trabajo será app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
