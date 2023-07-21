FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=veridocs.settings

EXPOSE 8080

CMD ["python", "veridocs/manage.py", "runserver", "0.0.0.0:8080"]