import json
import csv 

code = {'26': 'Dadra & Nagar Haveli', '35': 'Andaman & Nicobar Islands', '28': 'Andhra Pradesh', '12': 'Arunachal Pradesh', '18': 'Assam', '10': 'Bihar', '4': 'Chandigarh', '22': 'Chhattisgarh', '7': 'Delhi', '30': 'Goa', '24': 'Gujarat', '6': 'Haryana', '2': 'Himachal Pradesh', '1': 'Jammu & Kashmir', '20': 'Jharkhand', '29': 'Karnataka', '32': 'Kerala', '37': 'Ladakh', '31': 'Lakshadweep', '23': 'Madhya Pradesh', '27': 'Maharashtra', '14': 'Manipur', '17': 'Meghalaya', '15': 'Mizoram', '13': 'Nagaland', '21': 'Odisha', '34': 'Puducherry', '3': 'Punjab', '8': 'Rajasthan', '11': 'Sikkim', '33': 'Tamil Nadu', '36': 'Telangana', '16': 'Tripura', '5': 'Uttarakhand', '9': 'Uttar Pradesh', '19': 'West Bengal', '25': 'Daman & Diu', '0': 'National Average'}

def json_to_csv(json_data):
  keys = list(json_data.keys())
  header = sorted(keys)
  csv_data = []
  for k in header:
    csv_data.append(json_data[k])
  return csv_data, header

filename = "NAS_performance_scaled"

with open(filename + ".json", 'r') as f:
  json_data = json.loads(f.read())

# header = ["state_name", "grade", "subject","state_id","score","standard error", "category"]
# header = ["state_name", "grade", "subject","state_id","boys_score","boys_standard error","girls_score","girls_standard error","category"]
# header = ["state_name", "grade", "subject","state_id","rural_score","rural_standard error","urban_score","urban_standard error","category"]
# header = ["state_name", "grade", "subject","state_id","govt_score","govt_standard error","govt_aided_score","govt_aided_standard error","private_aided_score","private_aided_standard error","central_govt_aided_score","central_govt_standard error","category"]
header = ["state_name", "grade", "subject","state_id","sc_score","sc_standard error","st_score","st_standard error","obc_score","obc_standard error","general_score","general_standard error","general_category", "st_category", "obc_category"]
csv_data = []

grades = ["3", "5", "8", "10"]

for grade in grades:
  grade_data = json_data["grade_" + grade]
  subjects = sorted(list(grade_data.keys()))

  for sub in subjects:
    card_data = grade_data[sub]["social"]
    for x in range(len(card_data)):
      # temp = [code[str(card_data[x]["state_id"])], grade, sub, card_data[x]["state_id"], card_data[x]["rural_ss"], card_data[x]["rural_ss"], card_data[x]["urban_se"], card_data[x]["urban_se"], card_data[x]["category"]]
      # temp = [code[str(card_data[x]["state_id"])], grade, sub, card_data[x]["state_id"], card_data[x]["boys_ss"], card_data[x]["boys_se"], card_data[x]["girls_ss"], card_data[x]["girls_se"], card_data[x]["category"]]
      # temp = [code[str(card_data[x]["state_id"])], grade, sub, card_data[x]["state_id"], card_data[x]["govt_ss"], card_data[x]["govt_se"], card_data[x]["govt_aided_ss"], card_data[x]["govt_aided_se"], card_data[x]["pvt_ss"], card_data[x]["pvt_se"], card_data[x]["central_govt_ss"], card_data[x]["central_govt_se"], card_data[x]["category"]]
      temp = [code[str(card_data[x]["state_id"])], grade, sub, card_data[x]["state_id"], card_data[x]["gen_ss"], card_data[x]["gen_se"], card_data[x]["sc_ss"], card_data[x]["sc_se"], card_data[x]["st_ss"], card_data[x]["st_se"], card_data[x]["obc_ss"], card_data[x]["obc_se"], card_data[x]["gen_category"], card_data[x]["st_category"], card_data[x]["obc_category"]]
      csv_data.append(temp)

with open(filename + "_socialgroup.csv", 'w+') as csvfile:
  csv_writer = csv.writer(csvfile, delimiter=';')
  csv_writer.writerow(header)
  for row in csv_data:
    csv_writer.writerow(row)