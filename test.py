import json
from medify.models import ApprovedMedication 
import os
data_file = open(os.path.join("data", "medicinal.json"))
data = json.load(data_file)

ls= data["data"]
for item in ls:
	item["approval_date"] = item["approval_date"][-4:]+"-"+item["approval_date"][3:5]+"-"+item["approval_date"][:2]
	med= ApprovedMedication(**item)
	med.save()
	

data_file = open(os.path.join('data', 'illegal.json'))
data = json.load(data_file)

ls= data["data"]
for item in ls:
	med= IllegalMedication(**item)
	med.save()

    
data_file = open(os.path.join('data', 'pharmacies.json'))
data = json.load(data_file)

ls= data["data"]
for item in ls:
	pharmacy= Pharmacy(**item)
	pharmacy.save()
	
