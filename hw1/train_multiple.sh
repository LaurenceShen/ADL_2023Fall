#!/bin/bash
python3 run_swag_no_trainer.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --dataset_name ${1} \
  --max_seq_length 512 \
  --train_file train_new.json \
  --validation_file valid_new.json \
  --num_train_epochs 1 \
  --learning_rate 3e-5 \
  --output_dir multiple_model/
