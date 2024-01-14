#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

# __init__ and reload the FileStorage instance
storage = FileStorage()
storage.reload()
