""" Question 1: By default are django signals executed synchronously
 or asynchronously? Please support your answer with a code snippet that 
 conclusively proves your stance. The code does not need to be elegant
and production ready, we just need to understand your logic."""


""" 
Answer :
By default, Django signals are executed synchronously, meaning the signal handler 
 is executed immediately after the signal is sent.
"""

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received, starting work...")
    time.sleep(5) 
    print("Signal processing complete.")


user = User.objects.create(username='testuser')
print("User creation complete.")
