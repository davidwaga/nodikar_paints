from django.contrib import messages
from django.shortcuts import redirect, render

from products.models import Category, Product
from blog.models import Post
from .forms import QuoteRequestForm

def home(request):
    context = {
        "categories": Category.objects.all()[:6],
        "featured_products": Product.objects.filter(featured=True, available=True)[:6],
        "posts": Post.objects.filter(published=True)[:3],
    }
    return render(request, "core/home.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def quote(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your quote request has been received.")
            return redirect("quote")
    else:
        form = QuoteRequestForm()
    return render(request, "core/quote.html", {"form": form})
