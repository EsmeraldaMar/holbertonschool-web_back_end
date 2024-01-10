#!/usr/bin/env python3
""" Function that changes all topics of a school document based on the name """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ Updates the 'topics' field of all documents in 'mongo_collection'
    where the 'name' matches the specified school name
    """
    query = {"name": name}
    # query, check kwargs to match school by name
    new_values = {"$set": {"topics": topics}}
    # create function to set value topics
    # Using update_many to update all matching documents
    result = mongo_collection.update_many(query, new_values)
    
    # Returning the result of the update operation
    return result.modified_count