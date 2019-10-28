from scraping.mongodb_manager import *
from scraping.scraper import *
import pymongo
from bson.objectid import ObjectId
from datetime import date, timedelta

clt = MongodbManager('localhost', 27017)
scp = Scraper()


def update_routine(client, scraper):
    ids_mongodb = client.get_list_existing_jobs_ids()
    ids_nofluff = get_list_unique_ids(scraper.get_raw_list_all_jobs())

    ids_compared = compare_jobs_ids(ids_nofluff, ids_mongodb)

    for item in ids_compared[0]:
        client.archive_job(item)

    jobs_details = scraper.get_jobs_details(ids_compared[1])
    client.load_multiple_in_mongodb(jobs_details)


update_routine(clt, scp)

################

# Dealing with duplicates
#
# cursor = coll.aggregate(
#     [
#         {"$group": {"_id": "$id", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
#         {"$match": {"count": {"$gte": 2}}}
#     ]
# )

# for item in cursor:
#     print(item)
#     coll.delete_one({'_id': ObjectId(item['unique_ids'][0])})

# print(cursor)

################

# Adding date field

# cursor = coll.find({'status': {'$ne': 'ARCHIVED'}}).distinct('id')
#
# for item in cursor:
#     print(item)
#     # coll.delete_one({'_id': ObjectId(item['unique_ids'][0])})
#     coll.update_one({'id': item}, {"$set": {"dateAdded": str(date.today()),
#                                             "dateArchived": None}}, upsert=False)












