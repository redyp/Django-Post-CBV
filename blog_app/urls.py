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
    )
]