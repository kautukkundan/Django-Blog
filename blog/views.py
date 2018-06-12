from django.shortcuts import render

# Create your views here.
def post_list(req):
    return render(req, "blog/post_list.html", {})
