FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev bash tzdata openssl; \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime; \
    echo "America/Sao_Paulo" > /etc/timezone

# Dockerize Command
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install pipenv; \
    pipenv lock --requirements > requirements.txt; \
    pipenv lock --requirements --dev-only > requirements-dev.txt

RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

RUN cp /code/src/scripts/start.sh /usr/local/bin/entry-application
RUN chmod +x /usr/local/bin/entry-application

EXPOSE 8000