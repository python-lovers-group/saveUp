from django.contrib import admin
from app.models import Billing, Bill, Category

admin.site.register(Billing)
admin.site.register(Bill)
admin.site.register(Category)