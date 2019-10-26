from scraping.mongodb_manager import *

client = MongodbManager('localhost', 27017)

json_job = client.connect_to_nofluff().jobs.find_one()

# print(json_job['basics']['seniority'])

clean_json_job = dict()
clean_json_job["company"] = dict([
    ("name", json_job["company"]["name"]),
    ("size", json_job["company"]["size"])
])
clean_json_job["id"] = json_job["id"]
clean_json_job["basics"] = dict([
    ("category", json_job["basics"]["category"]),
    ("technology", json_job["basics"]["technology"]),
    ("seniority", json_job["basics"]["seniority"])
])
clean_json_job["requirements"] = dict([
    ("musts", [item["value"] for item in json_job["requirements"]["musts"]]),
    ("nices", [item["value"] for item in json_job["requirements"]["nices"]])
])
clean_json_job["description"] = json_job["details"]["description"]
clean_json_job["salary"] = json_job["essentials"]["salary"]
clean_json_job["location"] = dict([
    ("country", json_job["location"]["places"][0]["country"]["name"]),
    ("city", json_job["location"]["places"][0]["city"]),
    ("remote", json_job["location"]["remote"])
])
clean_json_job["benefits"] = json_job["benefits"]["benefits"]
clean_json_job["benefits"] = clean_json_job["benefits"] + json_job["benefits"]["officePerks"]
clean_json_job["status"] = json_job["status"]

print(clean_json_job)

id_to_update = 'AHLTAFOD'
collection = client.connect_to_nofluff().jobs
collection.update_one({'id': id_to_update}, {"$set": {"status": "ARCHIVED"}}, upsert=False)

