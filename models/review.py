#!/usr/bin/python3
"""
    Review Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of the Review Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.place_id = None
        self.user_id = None
        self.text = None
        super().__init__(*args, **kwargs)
