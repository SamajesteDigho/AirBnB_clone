#!/usr/bin/python3
"""
    State Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definition of the State Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.name = None
        super().__init__(*args, **kwargs)
