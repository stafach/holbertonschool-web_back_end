#!/usr/bin/env python3
"""Module that define list_all function"""


def list_all(mongo_collection):
    """lists all documents in a collection""" 
    return list(mongo_collection.find())
