#! /bin/bash

poetry run sam build --use-container
poetry run sam deploy --no-confirm-changeset