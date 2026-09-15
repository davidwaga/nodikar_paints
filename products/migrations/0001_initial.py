# Generated manually for the ColorCraft starter project.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="categories/")),
            ],
            options={"verbose_name_plural": "Categories", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sku", models.CharField(help_text="Unique stock keeping unit, e.g. INT-WHT-20L-001", max_length=50, unique=True)),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("short_description", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField()),
                ("pack_size", models.CharField(help_text="Examples: 1L, 4L, 20L, 25kg", max_length=30)),
                ("color", models.CharField(default="White", max_length=100)),
                ("stock_quantity", models.PositiveIntegerField(default=0)),
                ("reorder_level", models.PositiveIntegerField(default=5, help_text="Stock level at which the product should be reordered.")),
                ("cost_price", models.DecimalField(decimal_places=2, default=0, help_text="Purchase/cost price per pack in UGX.", max_digits=12)),
                ("selling_price", models.DecimalField(decimal_places=2, default=0, help_text="Selling price per pack in UGX.", max_digits=12)),
                ("image", models.ImageField(blank=True, null=True, upload_to="products/")),
                ("featured", models.BooleanField(default=False)),
                ("available", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="products", to="products.category")),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["sku"], name="products_pr_sku_5d9a9e_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["category", "available"], name="products_pr_categor_9e8d9b_idx"),
        ),
    ]
