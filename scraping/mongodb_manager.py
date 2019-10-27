from pymongo import MongoClient


# compare two sets and send back a list with :
# [0] = More on Mongodb => to be archived
# [1] = More on nofluff => to be added to Mongodb
def compare_jobs_ids(ids_nofluff, ids_mongodb):
    return [ids_mongodb.difference(ids_nofluff), ids_nofluff.difference(ids_mongodb)]


class MongodbManager:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)

    def connect_to_nofluff(self):
        db = self.client.nofluff
        return db

    # will only show jobs not archived
    def get_list_existing_jobs_ids(self):
        collection = self.connect_to_nofluff().jobs_clean
        ids = collection.find({'status': {'$ne': 'ARCHIVED'}}).distinct('id')
        return set(ids)

    def load_one_in_mongodb(self, job_details):
        collection = self.connect_to_nofluff().jobs_clean
        collection.insert_one(job_details)

    def load_multiple_in_mongodb(self, jobs_details):
        collection = self.connect_to_nofluff().jobs_clean
        for job in jobs_details:
            collection.insert_one(job)

    # change status from PUBLISHED to ARCHIVED
    def archive_job(self, id_to_update):
        collection = self.connect_to_nofluff().jobs_clean
        collection.update_one({'id': id_to_update}, {"$set": {"status": "ARCHIVED"}}, upsert=False)


