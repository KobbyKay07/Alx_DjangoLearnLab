from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/signup.html"

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