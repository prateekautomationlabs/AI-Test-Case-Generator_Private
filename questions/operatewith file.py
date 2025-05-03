#you got Json and you need to write it to csv
import csv


def write_json_to_file(filename, input_json):
    keys = input_json[0].keys()
    with open(filename, "w") as file:
       writer= csv.DictWriter(file, keys)
       writer.writeheader()
       writer.writerows(input_json)


fileName = "json_file.csv"
input_json= [
            {"test_case_id": "TC_001", "name": "Verify GET request", "url": "https://example.com/api",
              "method": "GET", "headers": {}, "body": None, "expected_status_code": 200,
              "expected_response": {"key": "value"} },
            {"test_case_id": "TC_002", "name": "Verify POST request", "url": "https://example.com/api",
              "method": "GET", "headers": {}, "body": {"greeting":"hello"}, "expected_status_code": 200,
              "expected_response": {"key": "value"} }
        ]

write_json_to_file(fileName, input_json)