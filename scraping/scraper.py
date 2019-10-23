import requests
import json
import time
from datetime import date


def get_details_job(job_id):
    res = requests.get('https://nofluffjobs.com/api/posting/{0}'.format(job_id))
    return json.loads(res.text)


class Scraper:

    def __init__(self):
        self.url = 'https://nofluffjobs.com/api/search/posting?region=pl'
        self.raw_list = []
        self.unique_ids = set()
        self.jobs_details = []
        self.date = date.today()

    def get_raw_list_all_jobs(self):
        response = requests.get(self.url)
        parsed = json.loads(response.text)
        self.raw_list = parsed['postings']

    def get_list_unique_ids(self):
        for item in self.raw_list:
            self.unique_ids.add(item['id'])

    def get_all_jobs_details(self):
        for i, job_id in enumerate(self.unique_ids, 1):
            self.jobs_details.append(get_details_job(job_id))

            # pacing
            if i % 30 == 0:
                print('{0} - {1}'.format(i, job_id))
                time.sleep(10.4)

    def get_new_jobs_only(self, new_jobs_ids):
        pass
