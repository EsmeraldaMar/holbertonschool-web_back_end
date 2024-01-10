#!/usr/bin/env python3
""" Python function that lists all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ mongo_collection will be the pymongo collection object
       Return an empty list if no document in the collection
    """
    documents = mongo_collection.find()
    return list(documents)
