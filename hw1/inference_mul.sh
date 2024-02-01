#!/bin/bash
python run_swag_no_trainer.py \
  --model_name_or_path ~/ADL/multiple_model/ \
  --dataset_name context.json \
  --train_file train_new.json \
  --validation_file valid_new.json \
  --test_file test_new.json \
  --max_seq_length 512 \
  --output_dir ~/ADL/multiple_result
