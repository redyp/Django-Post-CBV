from django.urls import path

from blog_app.views import BlogViews


urlpatterns = [
    path(
        '',
        BlogViews.as_view(
            template_name='index.html',
            title='Blog Post - Homepage'
        ),
        name='home'
    ),
    path(
        'blog/new/',
        BlogViews.as_view(
            template_name = 'blog/form.html',
            title='New Post'
        ),
        name='new_post'
    ),
]