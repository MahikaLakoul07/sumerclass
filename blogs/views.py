from django.shortcuts import get_object_or_404, render
from . models import Blogs, BlogCategory

def blogs(request):
    all_blogs = Blogs.objects.all()
    return render(request, 'basic/blogs.html', {'blogs': all_blogs})

def blog_detail(request, id):
    blogs = get_object_or_404(Blogs, id=id)
    return render(request, 'basic/blog_details.html', {'blog': blogs})
