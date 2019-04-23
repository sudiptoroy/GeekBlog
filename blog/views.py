from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # The mixins are for validations.
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . models import Post

"""
def home(request):
    
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/home.html', context)
"""

#  class based view for homepage. We have not followed the django convention for this. So we had to define those variable explicitly
class PostListview(ListView):
    model = Post
    template_name = 'blog/home.html'  #  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_poseted']
    paginate_by = 5  # Posts per page


class UserPostListview(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  #  <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5  # Posts per page

    def get_queryset(self):
        # Fetching the user from the url
        # If the user exits then it will be on user variable. If not then it will get 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_poseted')  # Returns the post of the user and order by date posted


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #  Overriding the form_valid method to get the current user
    def form_valid(self,form):
         form.instance.author = self.request.user
         return super().form_valid(form)  #  running form valid method in our parent class


#  This class is for updating a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   
    model = Post
    fields = ['title', 'content']

    #  Overriding the form_valid method to get the current user
    def form_valid(self,form):
         form.instance.author = self.request.user
         return super().form_valid(form)  #  running form valid method in our parent class

    def test_func(self):  # User cheking function
        post = self.get_object()
        
        if self.request.user == post.author:  # checking if the current loged in user is the author of the post
            return True
        return False


# This class is for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # After deleting a post it will automatically redirect to the homepage

    def test_func(self):  # User cheking function
        post = self.get_object()
        
        if self.request.user == post.author:  # checking if the current loged in user is the author of the post
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})


