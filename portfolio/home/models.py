from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Contact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    technologies = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=200, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.degree

class ProfessionalExperience(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company

class Skill(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=50)
    proficiency = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])  

    def __str__(self):
        return self.name