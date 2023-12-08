FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update \
    && apt-get install python3-dev default-libmysqlclient-dev gcc -y
RUN pip install --upgrade pip 
COPY requirements.txt /app/
RUN pip install -r reuirements.txt
COPY . /app/
COPY .env /app/.env
ENV $(cat /app/.env | xargs)
EXPOSE 8000