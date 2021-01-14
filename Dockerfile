FROM ubuntu:20.04

ENV EXERCISM_WORKSPACE=/exercism
RUN apt update

# Setup python requirements
RUN apt install -y curl python3-pip python-is-python3
RUN curl -sSL --retry 3 "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" | python \
    && python ~/.poetry/bin/poetry config virtualenvs.create false

# Setup python environment
RUN mkdir -p "$EXERCISM_WORKSPACE/python"
WORKDIR $EXERCISM_WORKSPACE/python
COPY python/pyproject.toml $EXERCISM_WORKSPACE/python
COPY python/poetry.lock $EXERCISM_WORKSPACE/python
RUN python ~/.poetry/bin/poetry install && rm -rf ~/.poetry
