
# def MyModel():
#   return "hello world"
from django.db import models

class MyModel(models.Model):
    # Define the fields for your model
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)