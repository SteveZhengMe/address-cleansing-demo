#! /bin/bash

swaggerhub api:update SteveZheng/AddressCleanseDemo --setdefault --file ./swagger/openapi.yaml

# get the error from swaggerhub:
if [ $? -ne 0 ]; then
    echo "Update Failed. Create a new version of the API"
    swaggerhub api:create SteveZheng/AddressCleanseDemo --setdefault --file ./swagger/openapi.yaml
    exit 0
fi
