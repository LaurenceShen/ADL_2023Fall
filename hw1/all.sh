#!/bin/bash
python3 convert_train.py --context_json_name ${1}
python3 convert_valid.py --context_json_name ${1}
python3 convert_test.py --test_json_name ${2} --context_json_name ${1}
./train_multiple.sh ${1}
./train_qa.sh ${1}

python3 run_swag_no_trainer.py \
  --model_name_or_path multiple_model \
  --dataset_name ${1} \
  --test_file test_new.json \
  --max_seq_length 512 \
  --output_dir multiple_result

python3 run_qa_no_trainer.py \
  --model_name_or_path qa_model \
  --dataset_name ${1} \
  --max_seq_length 512 \
  --doc_stride 128 \
  --test_file test_after_multichoice.json \
  --num_train_epochs 3 \
  --do_predict \
  --learning_rate 3e-5 \
  --output_dir qa_result/

python3 chinese.py --prediction_path ${3}
