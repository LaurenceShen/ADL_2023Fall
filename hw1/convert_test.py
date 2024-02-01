import json
import argparse
# -*- coding: UTF-8 -*-
parser = argparse.ArgumentParser(description="convert test.json into correct form")
parser.add_argument(
    "--test_json_name",
    type=str,
    default=None,
    help="The name of the test.json to use (via the datasets library).",
)
parser.add_argument(
    "--context_json_name",
    type=str,
    default=None,
    help="The name of the test.json to use (via the datasets library).",
)
args = parser.parse_args()
data_name = args.test_json_name
with open(data_name, encoding="utf8") as f:
    data = json.load(f)
with open(args.context_json_name, encoding="utf8") as f:
    context = json.load(f)

for i in range(len(data)):
    data[i]['answer'] = {}
    data[i]['answer']['answer_start'] = []
    data[i]['answer']['text'] = []
    data[i]['relevant'] = ""
    tmp = []
    for j in data[i]["paragraphs"]:
        tmp.append(context[j])
    data[i]["paragraphs"]=tmp
    #print(data[i]['question'])
#print(type(data))
with open("test_new.json", "w", encoding="utf8") as outfile:
    json.dump(data, outfile, ensure_ascii=False)
