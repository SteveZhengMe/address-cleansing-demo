#! /bin/bash

poetry run sam build --use-container
poetry run sam local start-api