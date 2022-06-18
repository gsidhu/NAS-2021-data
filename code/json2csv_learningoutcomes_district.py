import json
import csv 

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

filename = "NAS_LO_district"

with open("./json_data/" + filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

with open("./json_data/NAS_district_udise_codes.json", 'r') as f:
  codes = json.loads(f.read())

header = ['district_name', 'state_name', 'avg', 'created_at', 'district_id', 'grade', 'id', 'language', 'national_avg', 'question', 'state_avg', 'state_id', 'subject_code', 'total_student', 'updated_at']

csv_data = []

for dist in json_data:
  udise_code = dist['district_id']
  c, h = json_to_csv(dist)
  to_add = [codes[udise_code]["district_name"], codes[udise_code]["state_name"]]
  to_add.extend(c)
  csv_data.append(to_add)
  to_add = []

with open(filename + ".csv", 'w+') as csvfile:
  csv_writer = csv.writer(csvfile, delimiter=';')
  csv_writer.writerow(header)
  for row in csv_data:
    csv_writer.writerow(row)