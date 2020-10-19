from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'pub_date','is_published',]

