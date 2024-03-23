#!/usr/bin/python3
"""
    User Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of the User Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.email = None
        self.password = None
        self.first_name = None
        self.last_name = None
        super().__init__(*args, **kwargs)
