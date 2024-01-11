#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count and display the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"Total logs: {total_logs}")

    # Display count of each method type
    print("Count of each method:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"  {method}: {count}")

    # Count and display the number of GET requests to /status
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"GET requests to /status: {status_checks}")


if __name__ == "__main__":
    main()
