from django.shortcuts import render
from .models import Posts
# Create your views here.

def index(request):
    Post = Posts.objects.all()
    return render(request,'index.html',{'posts':Post})

def posts(request,pk):
    Post=Posts.objects.get(id=pk)
    return render(request,'posts.html',{'posts':Post})