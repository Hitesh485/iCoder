from django.shortcuts import render, HttpResponse, redirect
from . models import Contact
from django.contrib import messages
from blog . models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# HTML pages
def index (request):
    return render(request, 'home/index.html')

def about (request):
    return render(request, 'home/about.html')
    
def contact (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "⚠ Please fill contact form correctly")
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request, "✔️ Your message has been sent successfully")
    return render(request, 'home/contact.html')

def search (request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsAuthor, allPostsContent)
    params = {'allPosts':allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authentication API's
def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(fname, lname, username, email, pass1, pass2)
    # Check for error input
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")

        if not username.isalnum():
            messages.error(request, "Username should not contain special symbols")
        
        if (pass1 != pass2):
            messages.error(request, "Password do not match !")

    # Create the user
        else:
            myUser = User.objects.create_user(username, email, pass1)
            myUser.first_name = fname
            myUser.second_name = lname
            myUser.save()
            messages.success(request, "Your iCoder has been successfully created")
            return redirect('index')
    return render(request, 'home/signup.html')

def handleLogin (request):
    if request.method == "POST":
        loginEmail = request.POST['loginEmail']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username = loginEmail, password = loginPassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please try again!")

    return render(request, 'home/login.html')
    
def handleLogout (request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')
    return HttpResponse("handleLogout")