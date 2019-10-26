import requests
import json
import time
from datetime import date


def get_list_unique_ids(raw_list):
    unique_ids = set()
    for item in raw_list:
        unique_ids.add(item['id'])
    return unique_ids


def clean_job(json_job):
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

    return clean_json_job


class Scraper:

    def __init__(self):
        self.url_jobs = 'https://nofluffjobs.com/api/search/posting?region=pl'
        self.url_job = 'https://nofluffjobs.com/api/posting/'
        self.date = date.today()

    def get_raw_list_all_jobs(self):
        response = requests.get(self.url_jobs)
        parsed = json.loads(response.text)
        raw_list = parsed['postings']
        return raw_list

    def get_details_job(self, job_id):
        res = requests.get('{0}{1}'.format(self.url_job, job_id))
        return json.loads(res.text)

    def get_jobs_details(self, unique_ids):
        jobs_details = []
        for i, job_id in enumerate(unique_ids, 1):
            jobs_details.append(clean_job(self.get_details_job(job_id)))

            # pacing
            if i % 30 == 0:
                print('{0} - {1}'.format(i, job_id))
                time.sleep(10.4)
        return jobs_details

