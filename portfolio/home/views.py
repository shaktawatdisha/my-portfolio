from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact, Project

def index(request):
    print('index',request)
    projects = Project.objects.all()
    return render(request, 'home.html', {"projects":projects})

def project(request, id):
    project = Project.objects.get(id=id)
    print('➡ home/views.py:15 project:', project)
    return render(request, 'project.html', {"project":project})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not message:
            return JsonResponse({"error": "All fields are required."}, status=400)

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        print("Contact saved!")
        return JsonResponse({"message": "Your message has been sent successfully!"})

    return render(request, 'index.html')  

