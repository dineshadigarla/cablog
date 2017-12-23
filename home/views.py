from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import ProfileForm, UserForm
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
@transaction.atomic
def update_profile(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile(user=request.user)
        print("yes")

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('home:dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
