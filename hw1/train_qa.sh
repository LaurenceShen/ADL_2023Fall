#!/bin/bash
python3 run_qa_no_trainer.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --dataset_name ${1} \
  --max_seq_length 512 \
  --doc_stride 128 \
  --per_device_train_batch_size 1 \
  --train_file train_new.json \
  --validation_file valid_new.json \
  --num_train_epochs 5 \
  --learning_rate 1e-5\
  --with_tracking \
  --output_dir qa_model
