"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . views import (
    PostListview,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListview
)

from . import views


urlpatterns = [

    path('user/<str:username>', UserPostListview.as_view(), name="user-posts"),
    path('', PostListview.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),

    # For this we don't need to create a new template. Because it will use the post_form.html template
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),

    # This url pattern expect the template named post_confirm_delete.html
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"), 

    path('about/', views.about, name="blog-about"),
]
