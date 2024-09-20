from django.db.models.signals import post_save
from django.dispatch import receiver
from models import MyModel
import threading

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler called from thread:", threading.get_ident())

# Create a new MyModel instance
new_model = MyModel(name="Example")
new_model.save()