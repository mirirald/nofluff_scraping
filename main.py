from scraping.mongodb_manager import *
from scraping.scraper import *

scraper = Scraper()
client = MongodbManager('localhost', 27017)

raw_list = scraper.get_raw_list_all_jobs()
unique_ids = get_list_unique_ids(raw_list)
ids_nofluff = unique_ids

print(ids_nofluff)

ids_mongodb = client.get_list_existing_jobs_ids()

print(ids_mongodb)

compared_ids = compare_jobs_ids(ids_nofluff,ids_mongodb)

print('To archived : {0}'.format(compared_ids[0]))
print('New jobs : {0}'.format(compared_ids[1]))

# from full json to cleaner and flatter one
# need to select info by name
