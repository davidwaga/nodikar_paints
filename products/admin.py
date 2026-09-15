from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "pack_size",
        "color",
        "stock_quantity",
        "reorder_level",
        "cost_price",
        "selling_price",
        "stock_status",
        "available",
    )
    list_filter = (
        "category",
        "color",
        "featured",
        "available",
    )
    search_fields = (
        "sku",
        "name",
        "color",
        "pack_size",
        "description",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_editable = (
        "stock_quantity",
        "reorder_level",
        "cost_price",
        "selling_price",
        "available",
    )
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Product Identity", {
            "fields": ("sku", "name", "slug", "category")
        }),
        ("Product Details", {
            "fields": (
                "short_description",
                "description",
                "pack_size",
                "color",
                "image",
            )
        }),
        ("Inventory & Pricing", {
            "fields": (
                "stock_quantity",
                "reorder_level",
                "cost_price",
                "selling_price",
            )
        }),
        ("Website", {
            "fields": ("featured", "available", "created_at")
        }),
    )

    @admin.display(boolean=True, description="Low Stock")
    def stock_status(self, obj):
        return obj.is_low_stock
