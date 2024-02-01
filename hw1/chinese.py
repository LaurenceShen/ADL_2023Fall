import json
import csv
# -*- coding: UTF-8 -*-
import argparse
parser = argparse.ArgumentParser(description="convert test.json into correct form")
parser.add_argument(
    "--prediction_path",
    type=str,
    default=None,
    help="The name of the test.json to use (via the datasets library).",
)
args = parser.parse_args()
data_name = 'qa_result/eval_predictions.json'
with open(data_name, encoding="utf8") as f:
    data = json.load(f)

with open("prediction_new.json", "w", encoding="utf8") as outfile:
    json.dump(data, outfile, indent = 2, ensure_ascii=False)

with open("prediction_new.json", encoding="utf8") as outfile:
    prediction = json.load(outfile)

with open(args.prediction_path, "w", encoding="utf8") as output_csv:

    csv_writer = csv.writer(output_csv)
    
    header = ['id', 'answer']
    csv_writer.writerow(header)
    for i in prediction.keys():
        csv_writer.writerow([i, prediction[i]])
    #csv_writer.writerow(prediction.values())





