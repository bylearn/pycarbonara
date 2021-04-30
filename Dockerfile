FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache postgresql-dev \
    gcc python3-dev musl-dev bash tzdata openssl \
    chromium udev ttf-freefont zlib-dev jpeg-dev gcc musl-dev freetype-dev fribidi-dev \
    harfbuzz-dev lcms2-dev openjpeg-dev tcl-dev tiff-dev tk-dev libffi-dev make libevent-dev build-base; \
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

RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

RUN cp /code/src/scripts/start.sh /usr/local/bin/entry-application
RUN chmod +x /usr/local/bin/entry-application

EXPOSE 8000
