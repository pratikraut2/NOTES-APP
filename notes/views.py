from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Note

# Home (show only user's notes)
@login_required
def home(request):
    notes = Note.objects.filter(user=request.user)   # only logged-in user’s notes
    return render(request, 'notes/home.html', {'notes': notes})

# Add Note
@login_required
def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            messages.success(request, "Note added successfully ✅")
            return redirect("home")
        else:
            messages.error(request, "All fields are required!")
    
    return render(request, 'notes/add.html')

# Edit Note
@login_required
def edit(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)  # user restricted
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        messages.success(request, "Note updated successfully ✅")
        return redirect("home")
    return render(request, 'notes/edit.html', {'note': note})

# Delete Note
@login_required
def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        note.delete()
        messages.success(request, "Note deleted 🗑️")
        return redirect('home')
    return render(request, 'notes/delete.html', {'note': note})

# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        # ✅ Check if user entered an email
        if "@" in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username
            except User.DoesNotExist:
                username = username_or_email
        else:
            username = username_or_email

        # ✅ Authenticate with username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "notes/register/login.html")

# Signup
def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.success(request, "Account created 🎉 Please login")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            
    return render(request, 'notes/register/signup.html')


# Logout

@login_required
def logout_view(request):
    logout(request)
    return render(request, "notes/register/logout.html")