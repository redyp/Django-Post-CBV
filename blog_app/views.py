from django.shortcuts import render, redirect
from django.views.generic import View

from blog_app.form import PostForm
from blog_app.models import Post

# Create your views here.

posts = Post.objects.filter(published_date__isnull=False)
form = PostForm()

class BlogViews(View):

    template_name = ''
    title = ''

    def get(self, request, pk=None, *args, **kwargs):
        return render(request, self.template_name, {
            'title': self.title,
            'posts': posts,
            'form': form,
        })