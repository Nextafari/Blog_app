from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    """This function shows a list of all the posts we have in the database"""
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, slug):
    """This function renders a post using the slug to reference each post it is rendering"""
    posts = Post.objects.all()
    return render(request, 'post.html', {'post':get_object_or_404(Post, slug=slug), 'posts':posts})


def about(request):
    return render(request, 'about.html', {})

def display_media(request):
    images = Post.objects.get(...)
    context = {'images':images.image}
    return render(request, 'index.html', context)
    
    #return render(request, 'index.html', {'images': images.image})
