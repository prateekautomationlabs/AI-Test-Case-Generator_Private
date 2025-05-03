import csv
import os

import pytest

file_path = os.path.join(os.path.dirname(__file__),"data","data.csv")

def read_csv():
    data = []
    with open (file_path,"r") as f:
        reader=csv.DictReader(f)

        for row in reader:
            row["payload"]= eval(row["payload"]) if row["payload"] else {}
            row["headers"] =eval(row["headers"]) if row["headers"] else {}
            data.append(row)
    print(f"printing data {data}")
    return data

@pytest.mark.parametrize("row",read_csv())
def test_read_csv(row):
    if "name" in row["payload"]:
        print(row["payload"]["name"])
    else:
        print("no name in payload")





