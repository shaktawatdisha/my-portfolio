from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact, Project, Resume, ProfessionalExperience, Education,Skill

def index(request):
    resume = Resume.objects.filter(name__iexact="DISHA SHAKTAWAT").first()    
    edu = Education.objects.filter(resume=resume).first()
    print('➡ portfolio/home/views.py:8 edu:', edu)
    prof_exp = ProfessionalExperience.objects.filter(resume=resume)
    for exp in prof_exp:
        exp.responsibilities_list = exp.responsibilities.split(".") 
        print('➡ portfolio/home/views.py:12 exp:', exp.responsibilities_list)
    
    projects = Project.objects.all()
    skills = Skill.objects.all()
    mid_index = len(skills) // 2
    left_skills = skills[:mid_index]  
    right_skills = skills[mid_index:]  
    content = {
        "projects":projects, 
        'education':edu, 
        'professional_experience':prof_exp, 
        'resume':resume, 
        "left_skills": left_skills, 
        "right_skills": right_skills
    }
    return render(request, 'home.html', content)


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

