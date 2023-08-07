from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm

class PostView(View):
    '''вывод записи'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComments(View):
    '''добавление комментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


