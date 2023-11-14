FROM python:3.10.13-alpine3.17
WORKDIR /api
COPY poetry.lock ./
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry install
COPY . .
WORKDIR /api/core
EXPOSE 8000
CMD ["poetry","run","python","manage.py","runserver","0.0.0.0:8000"]