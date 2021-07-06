# docker-mailserver-admin
A sidecar container for management tasks of docker-mailserver

**This repo is currently in development.**

# How to run the dev server

`DOCKER_MAILSERVER_ADMIN_API_KEY=<your_testing_key> poetry run uvicorn docker_mailserver_admin_api:app`

# How to run tests

`tox -e unit_tests`

TODO: 
1. Create API (https://github.com/docker-mailserver/docker-mailserver/issues/1800)
2. Build Web UI around the API (https://github.com/docker-mailserver/docker-mailserver/issues/2049)
