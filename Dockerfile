ARG PYTHON_VERSION=3.8-slim
FROM python:$PYTHON_VERSION

MAINTAINER pyLODE Developers <https://github.com/RDFLib/pyLODE/graphs/contributors>

USER root

RUN apt-get update && \
	apt-get upgrade -y --allow-downgrades --allow-remove-essential --allow-change-held-packages

# install extra requirements for pyLODE-via-server
COPY requirements.server.txt /tmp/
RUN pip3 install -r /tmp/requirements.server.txt

# copy the current directory contents
ADD . /app

WORKDIR /app

# install pyLODE from source, ensures we always use the latest development branch
RUN python3 setup.py install

RUN cd ./pylode

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "--chdir", "/app/pylode", "server:api"]