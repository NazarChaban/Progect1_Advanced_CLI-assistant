# FROM python:3.12

# # docker build -t cli_assistant:latest -f Dockerfile .
# # docker run -it cli_assistant:latest

# COPY . /cli_assistant

# WORKDIR /cli_assistant

# RUN pip install poetry
# RUN poetry install

# ENTRYPOINT ["python", 'src/main.py']

FROM python:3.12

# RUN pip install poetry

COPY . /app

WORKDIR /app

# RUN poetry config virtualenvs.create false \
    # && poetry install --no-interaction --no-ansi
RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]
