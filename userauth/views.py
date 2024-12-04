from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model , logout 
from django.contrib.auth.decorators import login_required
from medium.models import Post
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncHour
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


@login_required
def baseadmin(request):
    # Fetching user data
    total_users = User.objects.count()

    
    # Fetch admin details
    admins = User.objects.all()

    context = {
        'admins': admins,
        'total_users': total_users,
        
    }
    return render(request, 'userauth/dashboard.html', context)

@login_required

def dashboard(request):
    # Get the current date to filter posts and user registrations created today
    now = timezone.now()
    start_time = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Aggregating posts by hour for users and authors
    user_posts_by_hour = Post.objects.filter(date_posted__gte=start_time, author__isnull=True) \
        .annotate(hour=TruncHour('date_posted')).values('hour') \
        .annotate(count=Count('id')).order_by('hour')

    author_posts_by_hour = Post.objects.filter(date_posted__gte=start_time, author__isnull=False) \
        .annotate(hour=TruncHour('date_posted')).values('hour') \
        .annotate(count=Count('id')).order_by('hour')

    # Aggregating total posts by hour
    total_posts_by_hour = Post.objects.filter(date_posted__gte=start_time) \
        .annotate(hour=TruncHour('date_posted')).values('hour') \
        .annotate(count=Count('id')).order_by('hour')

    # Aggregating user registrations by hour
    user_registrations_by_hour = User.objects.filter(date_joined__gte=start_time) \
        .annotate(hour=TruncHour('date_joined')).values('hour') \
        .annotate(count=Count('id')).order_by('hour')

    # Prepare the data for the charts
    hours = list(range(0, 24))  # Full 24 hours range
    user_data = [0] * 24
    author_data = [0] * 24
    post_data = [0] * 24
    user_registration_data = [0] * 24  # For registered users per hour

    # Fill in user posts data
    for post in user_posts_by_hour:
        user_data[post['hour'].hour] = post['count']

    # Fill in author posts data
    for post in author_posts_by_hour:
        author_data[post['hour'].hour] = post['count']

    # Fill in total posts data
    for post in total_posts_by_hour:
        post_data[post['hour'].hour] = post['count']

    # Fill in user registrations data
    for user in user_registrations_by_hour:
        user_registration_data[user['hour'].hour] = user['count']

    # Get total number of users and authors
    total_users = User.objects.count()
    authors = Post.objects.filter(author__isnull=False).values('author').distinct().count()
    total_posts = Post.objects.count()

    context = {
        'hours': hours,
        'user_data': user_data,
        'author_data': author_data,
        'post_data': post_data,  # Total posts for the second chart
        'user_registration_data': user_registration_data,  # Registered users per hour
        'total_users': total_users,
        'authors': authors,
        'total_posts': total_posts,
    }

    return render(request, 'userauth/dashboard.html', context)


@login_required
def adminnavbar(request):
    return render(request, 'userauth/adminnavbar.html')

@login_required
def usermanagement(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'userauth/usermanagement.html', context)

@login_required
def authorinfo(request):
    authors = Post.objects.filter(author__isnull=False).values('author').distinct()
    context = {
        'authors': authors,
    }
    return render(request, 'userauth/authorinfo.html', context)