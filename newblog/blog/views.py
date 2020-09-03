from django.shortcuts import render
from .models import Post

# Create your views here.

def list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts':posts})

