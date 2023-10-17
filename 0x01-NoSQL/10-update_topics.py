#!/usr/bin/env python3
"""Chane school topics
"""

import pymongo

def update_topics(mongo_collection, name, topics):
    """changes all topics based on name to match
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
