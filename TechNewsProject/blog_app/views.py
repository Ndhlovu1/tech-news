from django.shortcuts import render, get_list_or_404
from .models import Post

#Create a View to display the list of posts
def post_list(request):
    posts = Post.published.all()
    
    return render(request,'blog/post/list.html',  {'posts':posts})
    
    
#Single Post View
def post_detail(request, year, month, day, post):
    
    post = get_list_or_404(Post,    slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month = month,
                                    publish__day = day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post' : post})
    




