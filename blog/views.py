from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.conf import settings

# Create your views here.
def post_list(req):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(req, "blog/post_list.html", {'posts' : posts})
