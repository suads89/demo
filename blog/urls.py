from django.urls import path
from django.urls import include, path
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
    # path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]