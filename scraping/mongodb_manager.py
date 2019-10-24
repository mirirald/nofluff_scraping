from pymongo import MongoClient


class MongodbManager:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)

    def connect_to_nofluff(self):
        db = self.client.nofluff
        return db

    def get_list_existing_jobs_ids(self):
        collection = self.connect_to_nofluff().jobs
        ids = collection.find({}).distinct('id')
        return set(ids)

    def load_in_mongodb(self, jobs_details):
        collection = self.connect_to_nofluff().jobs
        for job in jobs_details:
            collection.insert_one(job)

    def clean_jobs(self):
        pass

    def compare_jobs_ids(self):
        pass

    def archive_jobs(self):
        pass


