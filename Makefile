.PHONY: help
help: # @HELP Print this message
help:
	@echo "TARGETS:"
	@grep -E '^.*: *# *@HELP' $(MAKEFILE_LIST)    \
	    | awk '                                   \
	        BEGIN {FS = ": *# *@HELP"};           \
	        { printf "  %-20s %s\n", $$1, $$2 };  \
	    '

.PHONY: setup
setup: # @HELP Build the development containers and install dependencies
setup: dev-build update

.PHONY: dev-build
dev-build: # @HELP Build the development containers
dev-build:
	@docker-compose build

.PHONY: update
update: # @HELP Install Python dependencies
update:
	@echo "Installing / updating dependencies ..."
	@docker-compose run homepage pip install --user -r requirements.txt
	@echo "Successfully built containers and installed dependencies."

.PHONY: up
up: # @HELP Start the dev server
up:
	@docker-compose up

KEYBASE_FILE ?= keybase.txt
ROBOTS_FILE ?= robots.txt.staging
ANALYTICSTXT_FILE ?= analytics.txt
SECURITYTXT_FILE ?= security.txt
SITEURL ?= http://localhost:8000

.PHONY: build
build: # @HELP Build the production assets
build:
	@docker build --build-arg siteurl=${SITEURL} --build-arg offenaccountid=${OFFEN_ACCOUNT_ID} -t offen/website -f build/Dockerfile .
	@rm -rf output && mkdir output
	@docker create --entrypoint=bash -it --name assets offen/website
	@docker cp assets:/code/homepage/output/. ./output/
	@cp build/${ROBOTS_FILE} ./output/robots.txt
	@cp build/${KEYBASE_FILE} ./output/keybase.txt
	@mkdir -p ./output/.well-known
	@cp build/${ANALYTICSTXT_FILE} ./output/.well-known/analytics.txt
	@cp build/${SECURITYTXT_FILE} ./output/.well-known/security.txt
	@docker rm assets
