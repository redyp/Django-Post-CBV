from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def publish_post(self):
        self.published_date = timezone.now()
        self.save()

    def text_as_list(self):
        return self.text.split('\n')