from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bloghome (request):
    return HttpResponse('this is bloghome')

def blogPost (request, slug):
    return HttpResponse(f"This is blogpost : {slug}")