from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post

#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'post_list.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_detail.html', {'posts': posts})

class HomePageView(TemplateView):
    template_name = 'blog/index.html'

class BlogHomePageView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(slug=self.kwargs.get('slug'))
        return context
    


