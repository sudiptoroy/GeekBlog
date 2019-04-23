from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

"""
different types of messages
message.debug
message.info
message.success
message.error
message.warning

"""

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # if it is a post request then send the from with the post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # if the form is valid get the username
            messages.success(request, f'Hello {username}. Log in bellow')
            return redirect('login')
    else:
        form = UserRegisterForm()  # Otherwise send the form only

    return render(request, 'users/register.html', {'form':form, 'title': 'Register'})

@login_required 
def profile(request):


    if request.method == 'POST':  # If user makes a post request for profile update
        u_form = UserUpdateForm(request.POST, instance=request.user)  #  then send the from with the post data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        #  if the forms are valid then save the data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated ')
            return redirect('profile')  # Redirect the user to his/her profile
  
            #  Note: We are redirecting the user to the profile page instead of fall down into the 
            #  render template function call, because of the "POST GET Redirect pattern"
            
    else:  #  if it is not a post request then simply show the current data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'users/profile.html', context)
