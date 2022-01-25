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
    path(
        'blog/draft',
        BlogViews.as_view(
            template_name='blog/draft.html',
            title='Draft Post'
        ),
        name='draft_post'
    ),
    path(
        'blog/draft/<int:pk>',
        BlogViews.as_view(

        ),
        name='publish_draft_post'
    ),
    path(
        'blog/save',
        BlogViews.as_view(
            save_as_draft=True
        ),
        name='save_post_as_draft'
    )
]