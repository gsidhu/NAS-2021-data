import json
import csv 

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

filename = "NAS_participation_district"

with open("./json_data/" + filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

with open("./json_data/NAS_district_udise_codes.json", 'r') as f:
  codes = json.loads(f.read())

header = ['district_name', 'state_name','central_govt_school', 'central_govt_school_count', 'created_at', 'district_id', 'female_gender', 'female_gender_count', 'general_social_group', 'general_social_group_count', 'govt_aided_school', 'govt_aided_school_count', 'govt_school', 'govt_school_count', 'grade', 'id', 'male_gender', 'male_gender_count', 'obc_social_group', 'obc_social_group_count', 'private_school', 'private_school_count', 'rural_location', 'rural_location_count', 'sc_social_group', 'sc_social_group_count', 'st_social_group', 'st_social_group_count', 'state_id', 'total_school', 'total_student', 'total_teacher', 'trans_gender', 'trans_gender_count', 'updated_at', 'urban_location', 'urban_location_count']

csv_data = []
for dist in json_data:
  c, h = json_to_csv(dist)
  to_add = [codes[dist["district_id"]]["district_name"], codes[dist["district_id"]]["state_name"]]
  to_add.extend(c)
  csv_data.append(to_add)
  to_add = []

with open(filename + ".csv", 'w+') as csvfile:
  csv_writer = csv.writer(csvfile, delimiter=';')
  csv_writer.writerow(header)
  for row in csv_data:
    csv_writer.writerow(row)