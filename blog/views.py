from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bloghome (request):
    return render(request, 'blog/blogHome.html')

def blogPost (request, slug):
    params = {"text":f"The text : {slug}"}
    return render(request, 'blog/blogPost.html', params)