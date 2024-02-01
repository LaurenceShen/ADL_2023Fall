#!/bin/bash

#convert public.jsonl into valid.json
python3 chinese.py --data_path ${1} --output_path valid.json
python3 chinese.py --data_path ${1} --output_path valid_with_id.json --with_id 1

python3 inference.py \
    --model_name_or_path model \
    --train_file valid.json \
    --validation_file valid.json \
    --source_prefix "summarize the text and find out the topic:  " \
    --num_beams 3 \
    --output_dir result/


python3 produce_submission.py \
	--data_path valid_with_id.json \
	--old_pred_path result/prediction.json \
	--predict_path ${2}
