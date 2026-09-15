from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    sku = models.CharField(
        max_length=50,
        unique=True,
        help_text="Unique stock keeping unit, e.g. INT-WHT-20L-001",
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    pack_size = models.CharField(
        max_length=30,
        help_text="Examples: 1L, 4L, 20L, 25kg",
    )
    color = models.CharField(max_length=100, default="White")
    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(
        default=5,
        help_text="Stock level at which the product should be reordered.",
    )
    cost_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="Purchase/cost price per pack in UGX.",
    )
    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        help_text="Selling price per pack in UGX.",
    )
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["sku"]),
            models.Index(fields=["category", "available"]),
        ]

    @property
    def is_low_stock(self):
        return self.stock_quantity <= self.reorder_level

    @property
    def profit_per_pack(self):
        return self.selling_price - self.cost_price

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name} ({self.sku})"
