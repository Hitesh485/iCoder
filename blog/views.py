from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def bloghome (request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost (request, slug):
    post = Post.objects.filter(slug = slug).first()
    params = {'post':post}
    return render(request, 'blog/blogPost.html', params)