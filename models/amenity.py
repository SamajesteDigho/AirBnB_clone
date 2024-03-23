#!/usr/bin/python3
"""
    Amenity Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of the Amenity Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.name = None
        super().__init__(*args, **kwargs)
