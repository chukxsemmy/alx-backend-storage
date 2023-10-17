#!/usr/bin/env python3
"""Insert a doc in Py
"""

import pymongo

def insert_school(mongo_collection, **kwargs):
    """Inserts a new doc in a collection school
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
