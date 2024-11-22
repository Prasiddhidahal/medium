from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model , logout 
from django.contrib.auth.decorators import login_required

User = get_user_model()  

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES) 
        if form.is_valid():
            
            new_user = form.save()

            
            usernames = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {usernames}!')

            # Authenticate the new user
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])

            # Log in the user and redirect
            if new_user is not None:
                login(request, new_user)
                return redirect('medium:index')  # Redirect to the home page
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'userauth/register.html', context)



@csrf_protect
def user_login(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in.")  
        return redirect('medium:index')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f'User with {email} does not exist')
            return render(request, "userauth/login.html", {})

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")  
            return redirect("medium:index")
        else:
            messages.warning(request, "Incorrect password. Please try again.")

    context = {}
    return render(request, "userauth/login.html", context)

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")


    return redirect('userauth:login')

#userprofile
@login_required
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
      
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.image = request.FILES.get('image')
        user.save()

        messages.success(request, "Your profile has been updated successfully!")
        

    return render(request, 'userauth/profile.html', {'user': request.user})