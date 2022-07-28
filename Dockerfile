FROM python:3

WORKDIR /usr/src/app
COPY . ./
COPY schema.ttl ./
RUN pip3.10 install --no-cache-dir -r requirements.txt
