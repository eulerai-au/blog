import os
import time
import json
from pymongo import MongoClient

# MongoDB configurations
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "benchmark_db"

def get_all_files(data_dir, extensions):
    """Recursively get files with specific extensions in a directory."""
    files = []
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

def write_test(data_dir):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    json_files = get_all_files(data_dir, [".json"])
    total_time = 0

    for file_path in json_files:
        if "_DONE" in file_path:
            continue
        with open(file_path, 'r') as f:
            content = json.load(f)
        collection_name = os.path.basename(file_path).split('.')[0]
        start_time = time.time()
        db[collection_name].insert_one(content)
        total_time += (time.time() - start_time)

    print(f"Total write time for MongoDB: {total_time} seconds")

def read_test():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    total_time = 0
    record_count = 0

    for collection_name in db.list_collection_names():
        start_time = time.time()
        records = list(db[collection_name].find())
        record_count += len(records)
        total_time += (time.time() - start_time)

    print(f"Total read time for MongoDB: {total_time} seconds")
    print(f"Number of records fetched: {record_count}")

if __name__ == "__main__":
    data_dir = os.path.expanduser("~/database_benchmark/graphy_raw_data/")
    write_test(data_dir)
    read_test()