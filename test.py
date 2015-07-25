import json
from medify.models import ApprovedMedication 

data_file = open('data\medicinal.json')
data = json.load(data_file)

ls= data["data"]
for item in ls:
	item["approval_date"] = item["approval_date"][-4:]+"-"+item["approval_date"][3:5]+"-"+item["approval_date"][:2]
	med= ApprovedMedication(**item)
	med.save()
	

data_file = open('data\illegal.json')
data = json.load(data_file)

ls= data["data"]
for item in ls:
	med= IllegalMedication(**item)
	med.save()

    
data_file = open('data\pharmacies.json')
data = json.load(data_file)

ls= data["data"]
for item in ls:
	pharmacy= Pharmacy(**item)
	pharmacy.save()
	
