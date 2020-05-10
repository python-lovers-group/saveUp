from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model is used to categorize user's bills.
    Fields:
    name: string
    """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = "categories"
        verbose_name = "category"

    def __str__(self):
        return f"<Category: {self.name}>"


class Billing(models.Model):
    """
    Billing model receives all the user's billing informations.

    Fields:
    user: User (FK)
    limit: int

    created_at: datetime
    updated_at: datetime
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    limit = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "billings"
        verbose_name = "billing"

    def __str__(self):
        return f"<Billing: {self.user}>"


class Bill(models.Model):
    """
    Bill model receives data about one, specified user's bill.

    Fields:
    billing: Billing (FK)

    price: float
    categories: Category
    where: string
    description: string

    created_at: datetime
    updated_at: datetime
    """

    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name="bills")

    price = models.FloatField()
    categories = models.ManyToManyField(Category)
    where = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "bills"
        verbose_name = "bill"

    def __str__(self):
        return f"<Bill: {self.price}, {self.where}>"


def users_billing(sender, instance, created, **kwargs):
    if created:
        Billing.objects.create(user=instance)


post_save.connect(users_billing, sender=User)
