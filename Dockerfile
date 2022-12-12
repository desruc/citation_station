FROM python:3.11.1-slim-bullseye

ARG DISCORD_TOKEN
ARG CHANNEL_ID
ARG HOUR_TO_SEND

ENV DISCORD_TOKEN=${DISCORD_TOKEN}
ENV CHANNEL_ID=${CHANNEL_ID}
ENV HOUR_TO_SEND=${HOUR_TO_SEND}

# Configure Poetry
ENV POETRY_VERSION=1.2.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache


# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Run your app
COPY . .

ENTRYPOINT ["poetry"]
CMD [ "run", "python", "-m", "citation_station"]