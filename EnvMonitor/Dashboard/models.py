# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PlantSpecimen(models.Model):
    plant_date = models.DateTimeField()
    plant_type = models.ForeignKey('PlantType', on_delete=models.SET_NULL, null=True)
    
class PlantType(models.Model):
    pass
    
class EnvReading(models.Model):
    pass