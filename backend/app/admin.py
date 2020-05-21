from django.contrib import admin
from django.contrib.auth.models import Group
from app.models import Billing, Bill, Category
from app.serializers import BillSerializer

admin.site.site_header = "saveUp admin page"


class BillAdmin(admin.ModelAdmin):
    list_display = ('description', 'price', 'categories_name', 'billing_owner')
    list_display_links = ('description',)
    list_editable = ('price',)
    list_filter = ('where', 'price')
    search_fields = ('description',)

    def billing_owner(self, obj):
        return obj.billing.user

    def categories_name(self, obj):
        return BillSerializer(obj).data['categories']


class InLineBill(admin.TabularInline):
    model = Bill
    extra = 1


class BillingAdmin(admin.ModelAdmin):
    inlines = (InLineBill,)
    list_display = ('user', 'balance')

    def balance(self, obj):
        return sum([bill.price for bill in Bill.objects.filter(billing=obj)])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'owner', 'bills_sum', 'bills_number')

    def category_name(self, obj):
        return obj.name

    def owner(self, obj):
        return obj.user

    def bills_sum(self, obj):
        return sum([bill.price for bill in Bill.objects.filter(billing__user=obj.user, categories__name__contains=obj.name)])

    def bills_number(self, obj):
        return len([bill for bill in Bill.objects.filter(categories__user=obj.user, categories__name__contains=obj.name)])


admin.site.register(Bill, BillAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)
