from django.shortcuts import render

# Create your views here.
def index(request):
    print('index',request)
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Home(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'project.html')
