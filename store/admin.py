from django.contrib import admin

from store import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection"]
    list_editable = ["unit_price"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "In Stock (Low)"
        elif product.inventory >= 10:
            return "In Stock"
        else:
            return "Out of Stock"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer_name"]
    list_select_related = ["customer"]

    def customer_name(self, order):
        return order.customer.first_name


admin.site.register(models.Collection)
