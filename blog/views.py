from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    return render(request, "blog/post_list.html", {
        "posts": Post.objects.filter(published=True)
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    recommended = Post.objects.filter(published=True).exclude(pk=post.pk)[:3]
    return render(request, "blog/post_detail.html", {
        "post": post,
        "recommended": recommended,
    })
