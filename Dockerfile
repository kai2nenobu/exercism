FROM python:3.8-slim

ENV EXERCISM_WORKSPACE=/exercism

# Setup python requirements
RUN apt update && apt install -y curl
RUN curl -sSL --retry 3 "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" | python \
    && python ~/.poetry/bin/poetry config virtualenvs.create false

# Setup python environment
RUN mkdir -p "$EXERCISM_WORKSPACE/python"
WORKDIR $EXERCISM_WORKSPACE/python
COPY python/pyproject.toml $EXERCISM_WORKSPACE/python
COPY python/poetry.lock $EXERCISM_WORKSPACE/python
RUN python ~/.poetry/bin/poetry install && rm -rf ~/.poetry
