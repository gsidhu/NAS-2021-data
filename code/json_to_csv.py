import json
import csv

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

filename = "NAS_performance_percentage_state"

with open(filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

list_size = len(json_data["state 1"])

header = ["state_name","grade","id","created_at","updated_at","subject","state_average", "national_average", "state_average_scaled_2021", "state_average_scaled_2017","below_basic","basic","proficient","advanced"]
# header = ["state_name","grade","id","created_at","updated_at","subject","boys","girls","trans_gender","boys_basic_and_below_basic","boys_proficient_and_advance","girls_basic_and_below_basic","girls_proficient_and_advance"]
# header = ["state_name","grade","id","created_at","updated_at","subject","urban","rural","rural_basic_and_below_basic","rural_proficient_and_advance","urban_basic_and_below_basic","urban_proficient_and_advance"]
# header = ["state_name","grade","id","created_at","updated_at","subject","govt","govt_aided","private","central_govt","govt_basic_and_below_basic","govt_proficient_and_advance","govt_aided_basic_and_below_basic","govt_aided_proficient_and_advance","private_basic_and_below_basic","private_proficient_and_advance","central_govt_basic_and_below_basic","central_govt_proficient_and_advance"]
# header = ["state_name","grade","id","created_at","updated_at","subject","sc","st","obc","general","sc_basic_and_below_basic","sc_proficient_and_advance","st_basic_and_below_basic","st_proficient_and_advance","obc_basic_and_below_basic","obc_proficient_and_advance","general_basic_and_below_basic","general_proficient_and_advance"]

csv_data = []
for x in range(1, 38):
  state_key = "state " + str(x)
  temp = [json_data[state_key][list_size-1]["state_name"]]
  count = 0
  for y in range(4):
    meta = [json_data[state_key][y]["grade"], json_data[state_key][y]["id"],
      json_data[state_key][y]["created_at"], json_data[state_key][y]["updated_at"]]

    sub_data = json_data[state_key][y]["data"]
    sub_keys = sorted(list(sub_data.keys()))
    
    for subject in sub_keys:
      result = sub_data[subject]
      temp2 = []
      temp2.extend(temp)
      temp2.extend(meta)

      cards = [subject, result["cards"]["state"], result["cards"]["national"],
              result["cards"]["comp_2021"],result["cards"]["comp_2017"],
              result["performance_level"]["state"]["below_basic"],
              result["performance_level"]["state"]["basic"],
              result["performance_level"]["state"]["proficient"],
              result["performance_level"]["state"]["advanced"]]
      temp2.extend(cards)

      # result = result["gender"]["state"]
      # gender = [subject,
      #   result["boys"],result["girls"],result["trans_gender"],
      #   result["boys_basic_and_below_basic"],result["boys_proficient_and_advance"],
      #   result["girls_basic_and_below_basic"], result["girls_proficient_and_advance"]
      # ]
      # temp2.extend(gender)
      # result = result["location"]["state"]
      # location = [subject,
      #   result["urban"],result["rural"],
      #   result["rural_basic_and_below_basic"],result["rural_proficient_and_advance"],
      #   result["urban_basic_and_below_basic"], result["urban_proficient_and_advance"]
      # ]
      # temp2.extend(location)
      # result = result["management"]["state"]
      # management = [subject,
      #   result["govt"],result["govt_aided"],result["private"],result["central_govt"],
      #   result["govt_basic_and_below_basic"],result["govt_proficient_and_advance"],
      #   result["govt_aided_basic_and_below_basic"], result["govt_aided_proficient_and_advance"],
      #   result["private_basic_and_below_basic"],result["private_proficient_and_advance"],
      #   result["central_govt_basic_and_below_basic"], result["central_govt_proficient_and_advance"]
      # ]
      # temp2.extend(management)
      # result = result["socialgroup"]["state"]
      # socialgroup = [subject,
      #   result["sc"],result["st"],result["obc"],result["general"],
      #   result["sc_basic_and_below_basic"],result["sc_proficient_and_advance"],
      #   result["st_basic_and_below_basic"], result["st_proficient_and_advance"],
      #   result["obc_basic_and_below_basic"],result["obc_proficient_and_advance"],
      #   result["general_basic_and_below_basic"], result["general_proficient_and_advance"]
      # ]
      # temp2.extend(socialgroup)

      csv_data.append(temp2)

  with open(filename[:-16] + json_data[state_key][list_size-1]["state_name"] + "_overall.csv", 'w+') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(header)
    for row in csv_data:
      csv_writer.writerow(row)
    csv_data = []