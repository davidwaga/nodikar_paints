from django.contrib import admin
from .models import QuoteRequest

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "product", "quantity", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "email")
