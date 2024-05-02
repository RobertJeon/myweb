from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .models import Comment

# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list :': post_list}
    return render(request, 'myweb/post_list.html',context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post':post}
    return render(request, 'myweb/post_detail.html', context)

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment(post=post, content=request.POST.get('content'), create_date=timezone.now())
    comment.save()
    return redirect('myweb:detail', post_id=post.id)