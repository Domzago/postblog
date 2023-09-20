from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def home(request):
    p = Paginator(Post.objects.all(), 2)
    page = request.GET.get('page')
    posts = p.get_page(page)

    return render(request, 'home.html', {'posts':posts})
