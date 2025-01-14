from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from .forms import RegisterForm, LoginForm, ProfileForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:login')

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:profile')

    return render(request, './blog/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    form = LoginForm(request, data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next') or 'accounts:profile')

    return render(request, './blog/login.html', {'form': form})


@login_required
def profile_view(request):
    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user,
    )

    if form.is_valid():
        form.save()
        return redirect('accounts:profile')

    return render(request, './blog/profile.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


