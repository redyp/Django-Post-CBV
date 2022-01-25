from django.forms import ModelForm

from blog_app.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ('created_date', 'published_date')