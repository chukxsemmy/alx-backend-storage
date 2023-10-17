#!/usr/bin/env python3
"""Where can I learn Py
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns list of school by specific topic
    """
    return mongo_collection.find({"topics": topic})
