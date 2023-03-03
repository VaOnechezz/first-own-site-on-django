from django.shortcuts import render, get_object_or_404 
from .models import Blog

def all_blogs(request):
    amount_of_blogs = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:5] #Выводить только 5, ордер бай-от старого к новому сорт по дате
    return render(request,'blog/all_blogs.html', { 'blogs':blogs,'total_blogs':amount_of_blogs}) #{})

def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})