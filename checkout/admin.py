from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )


admin.site.register(Order, OrderAdmin)
