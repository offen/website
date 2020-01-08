help:
	@echo "    setup"
	@echo "        Build the development containers and install dependencies."
	@echo "    update"
	@echo "        Install / update dependencies in the development containers."
	@echo "    build"
	@echo "        Build the production assets."

setup: dev-build update

dev-build:
	@docker-compose build

up:
	@docker-compose up

update:
	@echo "Installing / updating dependencies ..."
	@docker-compose run homepage pip install --user -r requirements.txt
	@echo "Successfully built containers and installed dependencies."

ROBOTS_FILE ?= robots.txt.staging
SITEURL ?= http://localhost:8000

build:
	@docker build --build-arg siteurl=${SITEURL} --build-arg offen-account-id=${OFFEN_ACCOUNT_ID} -t offen/website -f build/Dockerfile .
	@rm -rf output && mkdir output
	@docker create --entrypoint=bash -it --name assets offen/website
	@docker cp assets:/code/homepage/output/. ./output/
	@cp build/${ROBOTS_FILE} ./output/robots.txt
	@docker rm assets

.PHONY: setup build up
