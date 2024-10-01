FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt Makefile ./

RUN make deps

COPY . .