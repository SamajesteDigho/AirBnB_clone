#!/usr/bin/python3
"""
    Init file configuration
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
