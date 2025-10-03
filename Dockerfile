FROM python:3.11-alpine3.21

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations; python3 manage.py migrate
RUN python3 manage.py createsuperuser --noinput || true

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
