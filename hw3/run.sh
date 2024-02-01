#!/bin/bash

python3 inference.py --model_path ${1} \
                     --adapter_path ${2} \
                     --test_data ${3} \
                     --output_path ${4}

