import csv
from pathlib import Path
DATABASE=Path(__file__).parent/"oui.csv"
def normalise_mac(mac):
	mac=mac.replace(":","").replace("-","").replace(".","")
	return mac.strip().upper()
def load_database():
	database={}
	with open(DATABASE,"r",encoding="utf-8-sig",newline="") as file:
		reader=csv.DictReader(file)
		for row in reader:
			assignment=row.get("Assignment","").strip()
			organization=row.get("Organization Name","").strip()
			if not assignment or not organization:
				continue
			assignment=normalise_mac(assignment)
			database[assignment]=organization
		return database
def get_vendor(mac,database):
	mac=normalise_mac(mac)
	if len(mac)!=12:
		return "INVALID MAC ADDRESS"
	if any(c not in "0123456789ABCDEF" for c in mac):
		return "INVALID MAC ADDRESS"
	for prefix_length in (9,7,6):
		prefix=mac[:prefix_length]
		if prefix in database:
			return database[prefix]
	return "Unknown"

