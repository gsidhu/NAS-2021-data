import json
import csv 

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

# filename = "NAS_feedback_state"
# filename = "NAS_learning_outcomes_state"
# filename = "NAS_participation_state"
filename = "NAS_performance_percentage_state"

with open(filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

list_size = len(json_data["state 1"])

header = ["state_name"]
csv_data = []
for x in range(1, 38):
  state_key = "state " + str(x)
  for y in range(0, list_size-1):
    parsed_csv, parsed_header = json_to_csv(json_data[state_key][y])
    if y == 0 and x == 1:
      header.extend(parsed_header)
    temp = [json_data[state_key][list_size-1]["state_name"]]
    temp.extend(parsed_csv)
    csv_data.append(temp)

with open(filename + ".csv", 'w+') as csvfile:
  csv_writer = csv.writer(csvfile, delimiter=';')
  csv_writer.writerow(header)
  for row in csv_data:
    csv_writer.writerow(row)