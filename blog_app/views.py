from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

class BlogViews(View):

    template_name = ''
    title = ''

    def get(self, request, pk=None, *args, **kwargs):
        return render(request, self.template_name, {
            'title': self.title,
        })