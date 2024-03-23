#!/usr/bin/python3
"""
    Place Model file definition
    While inherit from the BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Definition of the Place Model based on the BaseModel"""
    def __init__(self, *args, **kwargs):
        self.city_id = None
        self.user_id = None
        self.name = None
        self.description = None
        self.number_rooms = None
        self.number_bathrooms = None
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
