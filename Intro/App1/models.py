from __future__ import unicode_literals
from django.db import models


class playerManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['fname']) < 2:
            errors["fname"] = "Names should have more than 1 letter"
        if len(postData['lname']) < 2:
            errors["lname"] = "Names should have more than 1 letter"
        if len(postData['favcolor']) < 2:
            errors["favcolor"] = "Colors should have more than 1 letter"
        if len(postData['more']) < 2:
            errors["more"] = "You need too fill out the more info tab (At least 10 letters)"

        return errors

# Create your models here.
class people(models.Model):
    first_name = models.CharField(max_length=45, default='')
    last_name = models.CharField(max_length=45, default='')
    favorite_color = models.CharField(max_length=45, default='')
    more_about_you = models.CharField(max_length=225, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = playerManager()