from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Post
from .forms import AuthorForm, PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages


@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'blog/index.html')

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        author_form = AuthorForm(request.POST)
        if post_form.is_valid() and author_form.is_valid():
            author = author_form.save()
            post = post_form.save(commit=False)
            post.author = author
            post.save()
            print(f"Imagen guardada en: {post.image.name}")
            messages.success(request, "El post se ha actualizado con éxito.")
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

def about(request):
    return render(request, 'blog/about.html')

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "El post se ha actualizado con éxito.")
            return redirect('list_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "El post se ha eliminado con éxito.")
        return redirect('list_posts')
    else:
        messages.warning(request, "El método no es permitido.")
        return redirect('list_posts')


def detail_posts(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail_posts.html', {'post': post})
