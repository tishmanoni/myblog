from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def list_view(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integar deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver the lastpage of results
        posts = paginator.page(paginator.num_pages)

        # posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts':posts})

def detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status = 'published', publish__year=year, publish__month = month, publish__day=day  )
    return render(request, 'blog/post/view.html', {'post':post})

