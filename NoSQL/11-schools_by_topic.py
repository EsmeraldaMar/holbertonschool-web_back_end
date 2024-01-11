#!/usr/bin/env python3
"""  Function that returns the list of school having a specific topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Args takes topic, and returns list of schools as result"""
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)
