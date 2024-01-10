#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Inserts doc based on kwargs, returns new id """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id