from scraping.mongodb_manager import MongodbManager
from scraping.scraper import *

scraper = Scraper()
client = MongodbManager('localhost', 27017)

raw_list = scraper.get_raw_list_all_jobs()
unique_ids = get_list_unique_ids(raw_list)
ids_nofluff = unique_ids

print(ids_nofluff)

ids_mongodb = client.get_list_existing_jobs_ids()

print(ids_mongodb)

print('To archived : {0}'.format(ids_mongodb.difference(ids_nofluff)))
print('New jobs : {0}'.format(ids_nofluff.difference(ids_mongodb)))
