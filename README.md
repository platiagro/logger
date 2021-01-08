# PlatIAgro Logger

[![Build Status](https://github.com/platiagro/logger/workflows/Python%20application/badge.svg)](https://github.com/platiagro/logger/actions?query=workflow%3A%22Python+application%22)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=platiagro_logger&metric=alert_status)](https://sonarcloud.io/dashboard?id=platiagro_logger)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Requirements

You may start the server locally or using a docker container, the requirements for each setup are listed below.

### Local

- [Python 3.7](https://www.python.org/downloads/)

### Docker

- [Docker CE](https://www.docker.com/get-docker)

## Quick Start

Make sure you have all requirements installed on your computer. Then, you may start the server using either a [Docker container](#run-using-docker) or in your [local machine](#run-local).

### Run using Docker

Then, build a docker image that launches the API server:

```bash
docker build -t platiagro/logger:0.2.0 .
```

Finally, start the API server:

```bash
docker run -it -p 8080:8080 \
  --name logger \
  platiagro/logger:0.2.0
```

### Run Local:

(Optional) Create a virtualenv:

```bash
virtualenv -p python3 venv
. venv/bin/activate
```

Install Python modules:

```bash
pip install .
```

Then, start the API server:

```bash
python -m logger.api
```

## Testing

Install the testing requirements:

```bash
pip install .[testing]
```

Use the following command to run all tests:

```bash
pytest
```

Use the following command to run lint:

```bash
flake8 --max-line-length 127 logger/
```

## API

See the [PlatIAgro Logger API doc](https://platiagro.github.io/logger/) for API specification.
