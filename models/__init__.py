#!/usr/bin/env python3
"""
Module for initializing storage engine
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call reload() method on this variable
storage.reload()
