import requests
import json
import time
from datetime import date


def get_list_unique_ids(raw_list):
    unique_ids = set()
    for item in raw_list:
        unique_ids.add(item['id'])
    return unique_ids


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
            jobs_details.append(self.get_details_job(job_id))

            # pacing
            if i % 30 == 0:
                print('{0} - {1}'.format(i, job_id))
                time.sleep(10.4)
        return jobs_details

    def get_new_jobs_only(self, new_jobs_ids):
        pass
