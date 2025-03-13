FROM python:3.12


ENV PYTHONUNBUFFERED=1
ENV COMPOSE_BAKE=true

RUN apt-get update && apt-get install -y build-essential && \
    pip3 install uwsgi

#instructions for docker compose watch
RUN useradd -ms /bin/sh -u 1001 app
USER app
WORKDIR /app

COPY --chown=app:app requirements.txt /app
RUN pip3 install -r /app/requirements.txt

COPY --chown=app:app . /app

EXPOSE 8000 
CMD ["uwsgi", "--ini", "/app/init.ini"]