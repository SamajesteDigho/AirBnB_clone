#!/usr/bin/python3
"""
    City Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of the City Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.state_id = None
        self.name = None
        super().__init__(*args, **kwargs)
