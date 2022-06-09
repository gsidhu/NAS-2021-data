import csv
import json
with open("NAS_performance_percentage_state.json", 'r') as f:
  data = json.loads(f.read())

code = {'26': 'Dadra & Nagar Haveli', '35': 'Andaman & Nicobar Islands', '28': 'Andhra Pradesh', '12': 'Arunachal Pradesh', '18': 'Assam', '10': 'Bihar', '4': 'Chandigarh', '22': 'Chhattisgarh', '7': 'Delhi', '30': 'Goa', '24': 'Gujarat', '6': 'Haryana', '2': 'Himachal Pradesh', '1': 'Jammu & Kashmir', '20': 'Jharkhand', '29': 'Karnataka', '32': 'Kerala', '37': 'Ladakh', '31': 'Lakshadweep', '23': 'Madhya Pradesh', '27': 'Maharashtra', '14': 'Manipur', '17': 'Meghalaya', '15': 'Mizoram', '13': 'Nagaland', '21': 'Odisha', '34': 'Puducherry', '3': 'Punjab', '8': 'Rajasthan', '11': 'Sikkim', '33': 'Tamil Nadu', '36': 'Telangana', '16': 'Tripura', '5': 'Uttarakhand', '9': 'Uttar Pradesh', '19': 'West Bengal', '25': 'Daman & Diu'}

for k in range(1, 38):
  data['state ' + str(k)].append({"state_name": code[str(k)]})

with open("NAS_performance_percentage_state.json", 'w+') as f:
  f.write(json.dumps(data))