import json
import jsonlines
import csv
# -*- coding: UTF-8 -*-

import argparse
parser = argparse.ArgumentParser(description="convert test.json into correct form")
parser.add_argument(
    "--data_path",
    type=str,
    default='data/public.json',
    help="The name of the test.json to use (via the datasets library).",
)
parser.add_argument(
    "--old_pred_path",
    type=str,
    default='valid_result_tmp_4_greedy/prediction.json',

    help="The name of the test.json to use (via the datasets library).",
)
parser.add_argument(
    "--predict_path",
    type=str,
    default='data/prediction_tmp4_greedy.jsonl',
    help="The name of the test.json to use (via the datasets library).",
)
args = parser.parse_args()
ans = []
with open(args.data_path, 'r') as f:
    data = json.load(f)

with open(args.old_pred_path, 'r') as f:
    old_pred = json.load(f)
for i in range(len(old_pred)):
    old_pred[i]['id'] = data[i]['id']
    ans.append(old_pred[i])
    #print(ans[i])
with jsonlines.open(args.predict_path, 'w') as f:
    for i in ans:
        f.write(i)
