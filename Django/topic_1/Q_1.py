# from django.db.models.signals import post_save
# import time
# from django.dispatch import receiver
# from .models import MyModel
# # from myapp.models import MyModel

# @receiver(post_save, sender=MyModel)
# def my_handler(sender, instance, **kwargs):
#     print("Signal handler called immediately after save")
#     # Perform long-running tasks here
#     time.sleep(5)  # Simulate a long-running operation
from django.db.models.signals import post_save
import time
from django.dispatch import receiver
from .models import MyModel  # Assuming MyModel is in the same directory
from django.db import models

class MyModel(models.Model):
    # Define the fields for your model
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler called immediately after save")
    # Perform long-running tasks here
    time.sleep(5)  # Simulate a long-running operation

# Create a new instance of MyModel
new_model = MyModel(name="Example Model", description="This is a sample description")
new_model.save()