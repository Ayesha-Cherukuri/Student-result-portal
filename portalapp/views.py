from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Result  # ✅ import Student and Result models


# ---------- Signup View ----------
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ✅ Automatically create a Student record for the new user
            Student.objects.create(user=user, roll_no='N/A', course='N/A')
            login(request, user)   # ✅ automatic login after signup
            messages.success(request, "Account created and logged in successfully!")
            return redirect('home')   # ✅ go to home page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'portalapp/signup.html', {'form': form})


# ---------- Login View ----------
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')   # ✅ after login go to home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'portalapp/login.html', {'form': form})


# ---------- Logout View ----------
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')   # ✅ after logout go to login page


# ---------- Home Page View ----------
@login_required
def home_view(request):
    return render(request, 'portalapp/home.html')


# ---------- Results Page View ----------
@login_required
def result_view(request):
    try:
        student_instance = Student.objects.get(user=request.user)
        results = Result.objects.filter(student=student_instance)
    except Student.DoesNotExist:
        results = []
        messages.warning(request, "No student record found for this user.")
    return render(request, 'portalapp/results.html', {'results': results})
