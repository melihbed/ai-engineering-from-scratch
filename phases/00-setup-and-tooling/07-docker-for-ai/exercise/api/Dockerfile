FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV UV_PROJECT_ENVIRONMENT=/venv
ENV PATH="/venv/bin:$PATH"

COPY pyproject.toml uv.lock* ./

RUN uv sync --no-dev

COPY api/ .

EXPOSE 5000

CMD ["python", "app.py"]

