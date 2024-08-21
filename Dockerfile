FROM python:3.12-alpine AS builder

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base

COPY Pipfile Pipfile.lock ./

RUN \
    pip install pipenv daphne && \
    pipenv install --deploy --ignore-pipfile --system

RUN python -c "import nltk;nltk.download('stopwords');nltk.download('punkt_tab');nltk.download('punkt')"

COPY sentiment ./sentiment
COPY settings ./settings
COPY templates ./templates
COPY manage.py ./
COPY model.pkl ./

FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

LABEL org.opencontainers.image.source=https://github.com/almazkun/django-sentimental

WORKDIR /app

RUN apk update && apk add --no-cache \
    libgomp libstdc++

COPY --from=builder /root/nltk_data /root/nltk_data
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/daphne /usr/local/bin/daphne
COPY --from=builder /app /app


ENTRYPOINT [ "daphne" ]
CMD [ "settings.asgi:application", "-b", "0.0.0.0", "-p", "8000" ]