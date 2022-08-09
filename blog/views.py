from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import BlogComment, Post
from django.contrib import messages

# Create your views here.
def bloghome (request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost (request, slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post)
    params = {'post':post, 'comments':comments}
    return render(request, 'blog/blogPost.html', params)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)

        comment = BlogComment(comment = comment, user = user, post = post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    
    return redirect(f"/blog/{post.slug}")