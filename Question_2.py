"""Question 2: Do django signals run in the same thread as the caller? 
Please support your answer with a code snippet that conclusively proves 
your stance. The code does not need to be elegant and production ready, 
we just need to understand your logic.
"""

"""
Answer :
Yes, by default, Django signals are executed in the same thread as the caller.

"""

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

print(f"Caller is running in thread: {threading.current_thread().name}")
user = User.objects.create(username='testuser')
