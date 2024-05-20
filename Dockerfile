# Dockerfile
FROM python:3.12

RUN apt-get update -y && \
	apt install -y wget make

RUN pip install --upgrade pip

WORKDIR /app

COPY ./ ./

RUN pip install --requirement requirements.txt
RUN pip install Flask
RUN pip install line-bot-sdk
RUN pip install ngrok
RUN pip install openai
RUN pip install python-dotenv

EXPOSE 8888