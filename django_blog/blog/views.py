from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from permissions import IsAuthor
from .models import Post
from .serializers import PostSerializer


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

@login_required
def profile(request):
    """
    Displays and allows editing of the user's profile.
    GET: Shows the current profile details.
    POST: Updates the user's profile if form is valid.
    """
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # redirect to the same profile page after update
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)

class ListView(generics.ListAPIView):
    '''
    Displays a list of all Posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailView(generics.RetrieveAPIView):
    '''
    Displays details of a specific Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreateView(generics.CreateAPIView):
    '''
    Allows creation of a new Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create posts

class UpdateView(generics.UpdateAPIView):
    '''
    Allows updating an existing Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor] # Only authors users can update posts

class DeleteView(generics.DestroyAPIView):
    '''
    Allows deletion of a Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor] # Only authors users can delete posts

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form_title'] = "Create Post"   # or "Edit Post"
    return context
