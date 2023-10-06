FROM python:3.8-slim-buster
WORKDIR /docker-escape-demo-via-SSRF
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install curl libcap2-bin -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh ./get-docker.sh
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "flask", "--app", "app", "run", "--debug", "--host=0.0.0.0"]
