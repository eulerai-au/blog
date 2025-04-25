import os
import time
import json
import psycopg2

# PostgreSQL configurations
DB_NAME = "benchmark_db"
DB_USER = "postgres"
DB_PASSWORD = "31415926"  # Update to your password
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

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

    with connect_db() as conn:
        with conn.cursor() as cursor:
            for file_path in json_files:
                if "_DONE" in file_path:
                    continue
                with open(file_path, 'r') as f:
                    content = json.load(f)
                table_name = os.path.basename(file_path).split('.')[0]
                start_time = time.time()
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (data JSONB);")
                cursor.execute(f"INSERT INTO {table_name} (data) VALUES (%s);", [json.dumps(content)])
                conn.commit()
                total_time += (time.time() - start_time)

    print(f"Total write time for PostgreSQL: {total_time} seconds")

def read_test():
    total_time = 0
    record_count = 0

    with connect_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                start_time = time.time()
                cursor.execute(f"SELECT * FROM {table_name};")
                records = cursor.fetchall()
                record_count += len(records)
                total_time += (time.time() - start_time)

    print(f"Total read time for PostgreSQL: {total_time} seconds")
    print(f"Number of records fetched: {record_count}")

if __name__ == "__main__":
    data_dir = os.path.expanduser("~/database_benchmark/graphy_raw_data/")
    write_test(data_dir)
    read_test()