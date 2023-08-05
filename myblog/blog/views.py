from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post

class PostView(View):
    '''вывод записи'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})