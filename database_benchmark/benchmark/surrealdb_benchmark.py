import os
import time
import json
import requests

# SurrealDB configurations
SURREALDB_URL = "http://127.0.0.1:8000/sql"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
DB_NAMESPACE = "test_namespace"
DB_DATABASE = "test_database"
AUTH = ("root", "31415926")  # Update to your password

def execute_query(query):
    response = requests.post(SURREALDB_URL, json={"query": query}, auth=AUTH, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error executing query: {response.text}")
    return response.json()

def get_all_files(data_dir, extensions):
    """Recursively get files with specific extensions in a directory."""
    files = []
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

def write_test(data_dir):
    json_files = get_all_files(data_dir, [".json"])
    total_time = 0

    for file_path in json_files:
        if "_DONE" in file_path:
            continue
        with open(file_path, 'r') as f:
            content = json.load(f)
        table_name = os.path.basename(file_path).split('.')[0]
        start_time = time.time()
        query = f"INSERT INTO {table_name} CONTENT {json.dumps(content)};"
        execute_query(query)
        total_time += (time.time() - start_time)

    print(f"Total write time for SurrealDB: {total_time} seconds")

def read_test():
    query = "SELECT * FROM *;"
    start_time = time.time()
    result = execute_query(query)
    print(f"Total read time for SurrealDB: {time.time() - start_time} seconds")
    print(f"Number of records fetched: {len(result)}")

if __name__ == "__main__":
    data_dir = os.path.expanduser("~/database_benchmark/graphy_raw_data/")
    execute_query(f"USE {DB_NAMESPACE} {DB_DATABASE};")  # Set namespace and database
    write_test(data_dir)
    read_test()