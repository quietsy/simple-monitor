FROM python:slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -v -r requirements.txt
COPY . /app

CMD ["python", "app.py"]
