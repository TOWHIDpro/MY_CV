from django.shortcuts import redirect, render, HttpResponseRedirect
from . forms import SignupForm, LoginForm, PasswordForm, user_profile_edit
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from . models import user_profile
from django.shortcuts import get_object_or_404




# Signup.
def signup_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                uname = form.cleaned_data['username']
                passw = form.cleaned_data['password1']
                user = authenticate(username=uname, password=passw)
                login(request, user)

                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('/')
        else:
            form =SignupForm()
            
        return render(request, 'signup_user/signup.html', {
            'form': form
        })
    else:
        return HttpResponseRedirect('/')

# Login
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                passw = form.cleaned_data['password']
                user = authenticate(username=uname, password=passw)
                if user is not None:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return HttpResponseRedirect('/')
                
        else:
            form = LoginForm()
        return render(request, 'signup_user/login.html', {
            'form': form
        })
    else:
        return HttpResponseRedirect('/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Password Change
@login_required(login_url="/enroll/login")
def passchange(request):
    if request.method == 'POST':
        form = PasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = PasswordForm(user=request.user)
    return render(request, 'signup_user/passchange.html', {
        'form': form,
        'name': request.user
    })

# SHOW PROFILE
def profile(request):
    user_details = user_profile.objects.get(user=request.user)
    return render(request, 'signup_user/profile.html', {
        'user_details': user_details
    })

#  EDIT PROFILE
def edit_profile(request):
    profile = get_object_or_404(user_profile, user=request.user)
    if request.method == 'POST':
        form = user_profile_edit(request.POST, request.FILES, instance=profile, )
        if form.is_valid():
            form.save()


    else:
        form = user_profile_edit(instance=profile)
    return render(request, 'signup_user/edit_profile.html', {
        'form': form,
        'instance': profile
    })
