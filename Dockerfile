FROM python:3 AS pylode-cli

# Upgrade the base-OS packages
RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \
    && apt-get clean \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge \
    && rm -rf /var/lib/apt/lists/*

# Initialise the python environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING="utf-8"

WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Install pyLODE source code as an editable package
COPY . ./
RUN pip install -e ./

# Run the pylode-cli command when containers built from this image are launched
ENTRYPOINT ["python", "-m", "pylode.cli"]
CMD ["--help"]


FROM pylode-cli AS pylode-server

# Install some additional packages required by the pylode server
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install bs4 falcon gunicorn validators

# Predefine default (empty) values for environment variables that can be used
# to customise the appearance and behaviour of the pylode-server
ENV \
    # Optional URL for a custom CSS stylesheet to be referenced in HTML responses
    CSS_URL="" \
    # MIME type for the resource at FAVICON_URL, if that is set (e.g. `image/png`)
    FAVICON_MIME="image/x-icon" \
    # Optional URL for a custom favicon image to be referenced in HTML responses
    FAVICON_URL="" \
    # Optional Google Analytics tag ID to be used to track requests to this server
    GTAGID="" \
    # Log threshold for pyLODE server log messages to appear in the logs.
    LOG_LEVEL="INFO" \
    # Port that the web server will listen for requests on
    PORT="8000"

# Run the pyLODE server when the container launches
ENTRYPOINT ["python", "-m", "pylode.server"]
CMD []

FROM pylode-server AS pylode-gunicorn

# Add GUnicorn to the installation
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install gunicorn

# Define additional GUnicorn-configuration environment variables
# Note: GUnicorn also respects `PORT` from the base image
ENV \
    # Configuration options for the GUnicorn web server that make it compatible with docker.
    # (Log to stdout and stderr, and ensure workers use tmpfs storage)
    GUNICORN_CMD_ARGS="--access-logfile - --error-logfile - --worker-tmp-dir /dev/shm" \
    # Number of worker processes that the GUnicorn web server will use to handle requests.
    # In production, you should set this to 2-4 x the number of CPU cores.
    WEB_CONCURRENCY=1

ENTRYPOINT ["gunicorn"]
CMD ["pylode.server:api"]
