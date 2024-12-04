from django.shortcuts import render, redirect
from .models import Author, Post
from .forms import AuthorForm, PostForm

def index(request):
    return redirect('list_posts')

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        author_form = AuthorForm(request.POST)
        if post_form.is_valid() and author_form.is_valid():
            author = author_form.save()
            post = post_form.save(commit=False)
            post.author = author
            post.save()
            return redirect('list_posts')
    else:
        post_form = PostForm()
        author_form = AuthorForm()
    return render(request, 'blog/create_post.html', {
        'post_form': post_form,
        'author_form': author_form,
    })

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/list_posts.html', {'posts': posts})

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains(query)) if query else []
    return render(request, 'blog/search_posts.html', {'results': results})