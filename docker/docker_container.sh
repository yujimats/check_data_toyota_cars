#!/bin/bash

docker run \
    -it \
    --rm \
    --name python3-ubuntu22_$1 \
    --volume $(pwd)/../:/home/check_data_toyota_cars/ \
    --volume /path/to/dataset/:/home/check_data_toyota_cars/dataset_pets:ro \
    --workdir /home/check_data_toyota_cars/ \
    yujimats/python3-ubuntu2204