from django.shortcuts import render, redirect
from steg.models import Users, Blog
from steg.forms import BlogForm, CommentForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):    
    form = BlogForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully..")
            return redirect('contact')

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def contact(request):
    key = ''
    if request.method == "POST":
        key = request.POST.get('key')
        blogs = Blog.objects.filter(title__icontains=key).order_by('-id')
    else:
        blogs = Blog.objects.all().order_by('-id')
    context = {
        'key':key,
        'blogs': blogs
    }

    return render(request, 'contact.html', context)

    
def edit_blog(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    ack = ''
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        updated_form = BlogForm(request.POST, request.FILES, instance=blog)
        if updated_form.is_valid():
            updated_form.save()
            messages.success(request, "Blog updated successfully..")
            return redirect('/contact/')
        else:
            ack = "Inavalid input.."
    
    context = {
        'ack':ack,
        'form': form    
    }

    return render(request, 'edit_blog.html', context)

def del_blog(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise(Http404)
    if blog.delete():
        messages.error(request, "Blog deleted..")
        return redirect('contact')
    return render(request, 'contact.html')

def view_blog(request, id):
    comment = CommentForm()
    blog = Blog.objects.get(id=id)

    ack = ""

    if request.method == "POST":
        comment = CommentForm(request.POST)
        comment.save()
        ack = "Your comment is published"

    context = {
        'ack' : ack,
        'comment':comment,
        'blog':blog
    }

    return render(request, 'blog.html', context)

def search_blog(request, key):
    blogs = Blog.objects.all()
    context = {
        'key':key,
        'blogs':blogs
    }
    return render(request, 'index.html', context)

from django.contrib.auth import login, authenticate, logout

def login_users(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user}")
            return redirect('contact')
        else:
            messages.error(request, "Invalid user details...")

    return render(request, 'login.html')