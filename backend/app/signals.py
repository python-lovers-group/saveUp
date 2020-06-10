from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Billing, Category


@receiver(post_save, sender=User)
def users_billing(sender, instance, created, **kwargs):
    if created:
        Billing.objects.create(user=instance)


@receiver(post_save, sender=User)
def users_default_categories(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(name="Food", user=instance)
        Category.objects.create(name="Health", user=instance)
        Category.objects.create(name="Entertainment", user=instance)
        Category.objects.create(name="Clothes", user=instance)
        Category.objects.create(name="Transport", user=instance)
        Category.objects.create(name="Education", user=instance)
        Category.objects.create(name="Other", user=instance)
