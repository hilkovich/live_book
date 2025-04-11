FROM python:3.12

WORKDIR /bot

COPY requirements.txt /bot

RUN pip install --upgrade pip && pip install -r /bot/requirements.txt

EXPOSE 8080

COPY ./ /bot

CMD ["python", "app.py"]
