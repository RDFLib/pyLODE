ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION} AS base
WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY pylode ./pylode
RUN pip install --no-cache-dir .

FROM base AS pylode-server
RUN pip install --no-cache-dir ".[server]"
EXPOSE 8000
CMD ["python", "-m", "pylode.server"]

FROM base AS pylode-gunicorn
RUN pip install --no-cache-dir ".[server]" gunicorn
EXPOSE 8000
CMD ["gunicorn", "pylode.server:api", "--bind", "0.0.0.0:8000"]

FROM base AS pylode
WORKDIR /data
ENTRYPOINT ["pylode"]
CMD ["--help"]
