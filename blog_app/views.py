from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from blog_app.form import PostForm
from blog_app.models import Post

# Create your views here.

# posts = Post.objects.filter(published_date__isnull=False).all()
# drafts = Post.objects.filter(published_date__isnull=True).all()
form = PostForm()

class BlogViews(View):

    template_name = ''
    title = ''
    save_as_draft = False

    def get(self, request, pk=None, *args, **kwargs):
        posts = Post.objects.filter(published_date__isnull=False).all()
        drafts = Post.objects.filter(published_date__isnull=True).all()
        if pk is not None:
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
        form = PostForm(request.POST)
        if self.save_as_draft:
            form.save()
            return redirect('home')
        post = form.save(commit=False)
        post.publish_post()
        return redirect('home')