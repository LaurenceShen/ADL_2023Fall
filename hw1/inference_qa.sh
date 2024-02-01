#!/bin/bash
python3 run_qa_no_trainer.py \
  --model_name_or_path ~/ADL/qa_model \
  --dataset_name context.json \
  --max_seq_length 512 \
  --doc_stride 128 \
  --train_file train_new.json \
  --validation_file valid_new.json \
  --test_file test_after_multichoice.json \
  --num_train_epochs 3 \
  --do_predict \
  --learning_rate 3e-5 \
  --output_dir ~/ADL/qa_result/
