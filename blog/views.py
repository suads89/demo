from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Post

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
