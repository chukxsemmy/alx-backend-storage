#!/usr/bin/env python3
"""List all docs in Py
"""


def list_all(mongo_collection):
    """Lists all docs in a collection
    """
    return [doc for doc in mongo_collection.find()]
