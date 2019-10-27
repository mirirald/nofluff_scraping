from scraping.mongodb_manager import *
from scraping.scraper import *
import pymongo
from bson.objectid import ObjectId

client = MongodbManager('localhost', 27017)
scraper = Scraper()

# UPDATE to put in a method/function
ids_mongodb = client.get_list_existing_jobs_ids()

coll = client.connect_to_nofluff().jobs_clean

ids_nofluff = get_list_unique_ids(scraper.get_raw_list_all_jobs())


ids_compared = compare_jobs_ids(ids_nofluff, ids_mongodb)

print(ids_compared[0])
print(ids_compared[1])

# for item in ids_compared[0]:
#     client.archive_job(item)
#
# jobs_details = scraper.get_jobs_details(ids_compared[1])
#
# client.load_multiple_in_mongodb(jobs_details)

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















