#!/bin/bash

#download train.json
gdown 1bLSF36SyZHZxp1NLthdJBaZYN2XXzr_l

python3 chinese.py --data_path train.json --output_path train_input.json

python3 qlora.py \
    --model_name_or_path yentinglin/Taiwan-LLM-7B-v2.0-chat \
    --use_auth \
    --output_dir model_tmp \
    --logging_steps 10 \
    --save_strategy steps \
    --data_seed 42 \
    --save_steps 250 \
    --save_total_limit 40 \
    --dataloader_num_workers 1 \
    --group_by_length \
    --logging_strategy steps \
    --remove_unused_columns False \
    --do_train \
    --lora_alpha 16 \
    --lora_modules all \
    --double_quant \
    --quant_type nf4 \
    --bits 4 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type constant \
    --gradient_checkpointing \
    --dataset train_input.json \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 2 \
    --max_steps 1500 \
    --eval_steps 187 \
    --learning_rate 0.0002 \
    --adam_beta2 0.999 \
    --max_grad_norm 0.3 \
    --lora_dropout 0.1 \
    --weight_decay 0.0 \
    --seed 0 \
