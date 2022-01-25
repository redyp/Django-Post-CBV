from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from blog_app.form import PostForm
from blog_app.models import Post

# Create your views here.

# posts = Post.objects.filter(published_date__isnull=False).all()
# drafts = Post.objects.filter(published_date__isnull=True).all()


class BlogViews(View):

    template_name = ''
    title = ''
    save_as_draft = False
    edit_post = False
    delete_post = False

    def get(self, request, pk=None, *args, **kwargs):
        posts = Post.objects.filter(published_date__isnull=False).all()
        drafts = Post.objects.filter(published_date__isnull=True).all()
        form = PostForm()
        if pk is not None:
            if self.edit_post:
                post = get_object_or_404(Post, pk=pk)
                form = PostForm(instance=post)
                return render(request, self.template_name, {
                    'title': self.title,
                    'form': form,
                    'pk': pk,
                })
            if self.delete_post:
                post = get_object_or_404(Post, pk=pk)
                post.delete()
                return redirect('home')
            draft = get_object_or_404(Post, pk=pk)
            draft.publish_post()
            return redirect('home')
        return render(request, self.template_name, {
            'title': self.title,
            'posts': posts,
            'drafts': drafts,
            'form': form,
        })
    
    def post(self, request, pk=None, *args, **kwargs):
        if pk:
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = PostForm(request.POST)
        if self.save_as_draft:
            form.save()
            return redirect('home')
        post = form.save(commit=False)
        post.publish_post()
        return redirect('home')