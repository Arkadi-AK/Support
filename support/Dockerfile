FROM python: 3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY ./support ./support

CMD ["python3", "./support/manage.py", "runserver", "0.0.0.0:8000"]