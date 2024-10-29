FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /templater_kassy/
WORKDIR /templater_kassy/backend
COPY requirements.txt /templater_kassy/backend
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /templater_kassy/backend
