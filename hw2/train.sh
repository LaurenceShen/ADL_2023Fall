#!/bin/bash

#convert public.jsonl into valid.json
#unzip data
#python chinese.py --data_path data/train.jsonl --output_path train.json
#python chinese.py --data_path data/public.jsonl --output_path public.json

python run_summarization_no_trainer.py \
    --model_name_or_path google/mt5-small \
    --train_file train_hw3.json \
    --validation_file public_hw3.json \
    --source_prefix "summarize the text and find out the topic:  " \
    --num_beams 3 \
    --num_train_epoch 1 \
    --output_dir model_tmp/ \
