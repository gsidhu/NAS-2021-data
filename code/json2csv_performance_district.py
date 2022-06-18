import json
import csv 

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

with open("./json_data/NAS_district_udise_codes.json", 'r') as f:
  codes = json.loads(f.read())

filename = "NAS_performance_percentage_district"

with open("./json_data/" + filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

dist_keys = list(json_data.keys())

header = ["district_name", "state_name", "udise_district_code", "grade", "updated_at", "created_at", "district_id", "state_id", "subject"]
header_cards = ["district_percentage", "district_standard_error", "district_below_basic", "district_basic", "district_proficient", "district_advanced", "state_percentage", "state_standard_error", "state_below_basic", "state_basic", "state_proficient", "state_advanced", "national_percentage", "national_standard_error", "national_below_basic", "national_basic", "national_proficient", "national_advanced"]

csv_data = []

for dist in dist_keys:
  udise_code = dist[dist.find("_")+1:]
  for grade_data in json_data[dist]:
    data = grade_data["data"]
    subjects = sorted(list(data.keys()))
    for sub in subjects:
      card_data = data[sub]["cards"]
      performance_level_data = data[sub]["performance_level"]
      temp = [codes[udise_code]["district_name"], codes[udise_code]["state_name"], udise_code,
        grade_data['grade'], grade_data["updated_at"], grade_data["created_at"], grade_data["district_id"], grade_data["state_id"],
        sub, card_data["district"], card_data["se_district"], performance_level_data["district"]["below_basic"], performance_level_data["district"]["basic"], performance_level_data["district"]["proficient"], performance_level_data["district"]["advanced"],
        card_data["state"], card_data["se_state"], performance_level_data["state"]["below_basic"], performance_level_data["state"]["basic"], performance_level_data["state"]["proficient"], performance_level_data["state"]["advanced"],
        card_data["national"], card_data["se_national"], performance_level_data["national"]["below_basic"], performance_level_data["national"]["basic"], performance_level_data["national"]["proficient"], performance_level_data["national"]["advanced"]
      ]
      # gender_data = data[sub]["socialgroup"]
      # temp = [codes[udise_code]["district_name"], codes[udise_code]["state_name"], udise_code,
      #   grade_data['grade'], grade_data["updated_at"], grade_data["created_at"], grade_data["district_id"], grade_data["state_id"],
      #   sub
      # ]
      # c, h = json_to_csv(gender_data['district'])
      # temp.extend(c)
      csv_data.append(temp)
      temp = []

# header.extend(h)
header.extend(header_cards)

with open(filename + "_overall.csv", 'w+') as csvfile:
  csv_writer = csv.writer(csvfile, delimiter=';')
  csv_writer.writerow(header)
  csv_writer.writerows(csv_data)