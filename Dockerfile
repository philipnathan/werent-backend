FROM python:3.12-alpine3.20

WORKDIR /backend

RUN apk add --no-cache \
    mysql-client \
    gcc \
    musl-dev \
    mysql-dev \
    python3-dev \
    libffi-dev

RUN pip install --upgrade pip --no-cache-dir && \
    pip install pipenv --no-cache-dir \
    flask-migrate

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --ignore-pipfile

COPY . .

EXPOSE 5000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]