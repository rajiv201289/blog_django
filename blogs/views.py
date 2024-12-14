from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

import blog
from blogs.forms import BlogForm, BlogPostForm
from .models import Blog,BlogPost



# Create your views here.

def index(request):
    """ This is the home page for the app blogs """
    return render(request,'blogs/index.html')
@login_required
def blogs_page(request):
    """ This page shows all the blogs on the website  """
    all_blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context={'all_blogs':all_blogs}
    return render(request,'blogs/blogs_page.html',context)

@login_required
def blog_posts(request,blog_id):
    """ This page shows all the posts related to a particular blog """
    blog = Blog.objects.get(id=blog_id)
    #Make sure the blog post belongs to the current user
    # if blog.owner != request.user:
    #     raise Http404
    check_blog_owner(blog.owner,request)
    
    posts = blog.blogpost_set.order_by('-date_added')
    context={'blog':blog,'posts':posts}
    return render(request,'blogs/blog_posts.html',context)

@login_required
def new_blog(request):
    """ Adding a new blog  """
    if request.method != 'POST':
        # No data is submitted:blank form
        form = BlogForm()
        
    else:
        #post data submitted : precess data
        form=BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs_page')
        
    # Displaying a blank or invalid form
    context={'form':form}    
    return render(request,'blogs/new_blog.html',context)
    
@login_required   
def new_post(request,blog_id):
    """  Addin a new post to a particular blog """
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        # NO data is submited; creat blank form
        form=BlogPostForm()
    else:
        # data is submitted;process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog_posts',blog_id=blog_id)
    # Display a blank or invalid form
    context={'blog':blog,'form':form}    
    return render(request,'blogs/new_post.html',context)       
        
    
@login_required    
def edit_post(request,post_id):
    """ Here we edit the post  """
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # initial request;pre filled form with the current post
        form=BlogPostForm(instance=post)
    else:
        # Post data submitted;process data.
        form=BlogPostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts',blog_id=blog.id)
    
    context={'post':post,'blog':blog,'form':form}
    return render(request,'blogs/edit_post.html',context)
        
        
# Deleting post
@login_required
def delete_post(request,post_id):
    post=BlogPost.objects.get(id=post_id)
    blog=post.blog
    if blog.owner != request.user:
        raise Http404
    post.delete()
    return redirect('blogs:blog_posts',blog_id=blog.id)


@login_required
def delete_blog(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404
    blog.delete()
    return redirect('blogs:blogs_page')
    

#My functions
def check_blog_owner(owner,request):
    if owner != request.user:
        raise Http404