from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from .models import Post
from .serializers import PostSerializer
from django.views.generic import CreateView


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

class List_View(generics.ListAPIView):
    '''
    Displays a list of all Posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Detail_View(generics.RetrieveAPIView):
    '''
    Displays details of a specific Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class Create_View(generics.CreateAPIView):
    '''
    Allows creation of a new Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create posts

class Update_View(generics.UpdateAPIView):
    '''
    Allows updating an existing Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor] # Only authors users can update posts

class Delete_View(generics.DestroyAPIView):
    '''
    Allows deletion of a Post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor] # Only authors users can delete posts
