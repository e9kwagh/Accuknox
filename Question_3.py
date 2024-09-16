"""
Question 3: By default do django signals run in the same database
transaction as the caller? Please support your answer with a code
snippet that conclusively proves your stance. The code does not need
to be elegant and production ready, we just need to understand your logic.
"""

"""
Answer :
By default, Django signals run within the same database transaction as the caller.
"""

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executed inside the same transaction.")
    print(f"Transaction active: {transaction.get_connection().in_atomic_block}")


with transaction.atomic():
    user = User.objects.create(username='testuser')
    print(f"Transaction active (in caller): {transaction.get_connection().in_atomic_block}")
