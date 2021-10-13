FROM mailserver/docker-mailserver:latest

# Update and install pip
RUN apt-get -qq update
RUN apt-get -qq install python3-pip -y
RUN apt-get -qq clean
RUN apt-get -qq autoclean

# Build wheel
RUN python3 -m pip install poetry
#RUN mkdir /tmp/build-admin-api
#COPY docker_mailserver_admin_api /tmp/build-admin-api
#COPY poetry.lock /tmp/build-admin-api
#COPY pyproject.toml /tmp/build-admin-api
#RUN cd /tmp/build-admin-api && poetry build

# Remove leftovers
#RUN rm /tmp/build-admin-api

# Install python application
RUN mkdir /opt/docker_mailserver_admin_api
COPY docker_mailserver_admin_api /opt/docker_mailserver_admin_api
COPY poetry.lock /opt/docker_mailserver_admin_api
COPY pyproject.toml /opt/docker_mailserver_admin_api
COPY admin-api-supervisor.conf /etc/supervisor/conf.d/
RUN cd /opt/docker_mailserver_admin_api && poetry install --no-dev

# Caddy installation
RUN apt-get install -y debian-keyring debian-archive-keyring apt-transport-https
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | tee /etc/apt/trusted.gpg.d/caddy-stable.asc
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
RUN apt-get update --allow-releaseinfo-change
RUN apt-get install caddy
COPY Caddyfile /etc/caddy/Caddyfile

# Remove caddy leftovers
RUN rm /etc/apt/trusted.gpg.d/caddy-stable.asc
RUN rm /etc/apt/sources.list.d/caddy-stable.list