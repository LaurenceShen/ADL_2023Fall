import json
import jsonlines
import csv
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

data_name = args.data_path
new_d = []
public = []
with jsonlines.open(data_name, "r") as data:
    with open(args.output_path, "w", encoding="utf-8") as outfile:
        for d in data:
            d['text'] = d['maintext']
            d['summary'] = ""
            keys = [];
            for i in d.keys():
                if (i != 'text' and i != 'summary'):
                    keys.append(i)
            for i in keys:
                if i == 'id' and args.with_id:
                    continue
                del d[i]
            new_d.append(d)
        json.dump(new_d, outfile, indent = 2, ensure_ascii=False)

'''
with open("prediction_new.json", encoding="utf8") as outfile:
    prediction = json.load(outfile)

with open(args.prediction_path, "w", encoding="utf8") as output_csv:

    csv_writer = csv.writer(output_csv)
    
    header = ['id', 'answer']
    csv_writer.writerow(header)
    for i in prediction.keys():
        csv_writer.writerow([i, prediction[i]])
    #csv_writer.writerow(prediction.values())
'''




