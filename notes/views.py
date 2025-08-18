from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Note

def home(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'notes/home.html', context)

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect("home")  # Redirect to home or notes list page after saving
        else:
            return render(request, 'notes/add.html', {"error": "All fields are required!"})
    
    return render(request, 'notes/add.html')


def edit(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return redirect("home")
    return render(request, 'notes/edit.html', {'note': note})

def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('home')  # safely sends user back
    return render(request, 'notes/delete.html', {'note': note})

def login(request):
    # Placeholder for login logic
    return render(request, 'notes/register/login.html')

def signup(request):
    # Placeholder for signup logic
    return render(request, 'notes/register/signup.html')

def logout(request):
    # Placeholder for logout logic
    return redirect('home')  # Redirect to home after logout