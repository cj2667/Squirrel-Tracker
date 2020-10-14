from django.db import models

# Create your models here.
class SquirrelDetail:
    def __init__(self, Latitude, Longitude, Unique_Squirrel_ID):
        self.Latitude = Latitude
	self.Longitude = Longitude
	self.Unique = Unique
	self.Unique_Squirrel_ID = Unique_Squirrel_ID

    def save(self):
	return None

    def SquirrelSightingForm(self, request_method):
	return None

