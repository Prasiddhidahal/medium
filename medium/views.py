from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


#medium Views
def index(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PostForm()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'blog/index.html', context)

def edit(request, id):
    print('Edit')
    post = Post.objects.get(id=id)  
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect('medium:index')  
    else:
        
        form = PostForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/edit.html', context)

def view(request,id):
    post= Post.objects.get(id=id)
    
    context = {
        'post': post,
        
    }
    return render(request, 'blog/view.html', context)

def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('medium:index')  
    

def create_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PostForm()
    context = {
       
        'form': form,
    }
    
    return render(request, 'blog/create.html', context)
