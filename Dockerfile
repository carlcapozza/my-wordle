
FROM python:3.9-slim AS base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

FROM base AS test

RUN pip install pytest

RUN pytest --maxfail=1 --disable-warnings

FROM base AS production

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
