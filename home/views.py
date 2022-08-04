from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return render(request, 'home/index.html')

def about (request):
    # return HttpResponse('about')
    return render(request, 'home/about.html')
    
def contact (request):
    return render(request, 'home/contact.html')
    