import json
import jsonlines
import csv
from utils import get_prompt, get_bnb_config
# -*- coding: UTF-8 -*-

import argparse
parser = argparse.ArgumentParser(description="convert test.json into correct form")
parser.add_argument(
    "--data_path",
    type=str,
    default=None,
    help="The name of the test.json to use (via the datasets library).",
)
parser.add_argument(
    "--output_path",
    type=str,
    default=None,
    help="The name of the test.json to use (via the datasets library).",
)
parser.add_argument(
    "--with_id",
    type=int,
    default=0,
    help="The name of the test.json to use (via the datasets library).",
)
args = parser.parse_args()
new_d = []
with open(args.data_path, "r", encoding="utf-8") as f:
    with open(args.output_path, "w", encoding="utf-8") as outfile:
        data = json.load(f)
        for d in data:
            if (d.get('output') == None):
                d['output'] = ""
            d['input'] = get_prompt(d['instruction']) 
            #d['input'] = get_prompt(d['instruction']) + "。 " + d['output']
            keys = [];
            if not args.with_id:
                del d['id']
            new_d.append(d)
        json.dump(new_d, outfile, indent = 2, ensure_ascii=False)
