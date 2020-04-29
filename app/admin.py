from django.contrib import admin
from app.models import Billing, Category, Bill

admin.site.register(Billing)
admin.site.register(Bill)
admin.site.register(Category)
