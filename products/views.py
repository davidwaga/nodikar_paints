from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def product_list(request):
    products = Product.objects.filter(available=True).select_related("category")
    category = request.GET.get("category")
    if category:
        products = products.filter(category__slug=category)
    return render(request, "products/product_list.html", {
        "products": products,
        "categories": Category.objects.all(),
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related = Product.objects.filter(
        category=product.category, available=True
    ).exclude(pk=product.pk)[:4]
    return render(request, "products/product_detail.html", {
        "product": product,
        "related": related,
    })
