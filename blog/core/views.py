from django.shortcuts import render
from .models import Blog_Model
from django.http import  HttpResponseRedirect

from django.urls import reverse



# Create your views here.

def home(request):
    all_blog = Blog_Model.objects.all()
    return render(request,'home.html',{'blogs':all_blog})


def addBlog(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['description']
        
        newBlog = Blog_Model.objects.create(name=name,title=title,description=description)
        newBlog.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'form.html')

def updateBlog(request,pk):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['description']
        Blog_Model.objects.filter(id=pk).update(name=name,title=title,description=description)
        #blog.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'update.html')
        

def deleteBlog(request,pk):
    blog = Blog_Model.objects.get(id=pk)
    blog.delete()
    return HttpResponseRedirect(reverse('home'))
