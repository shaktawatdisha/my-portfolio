from django.contrib import admin
from .models import Contact, Project, Resume, Education, ProfessionalExperience, Skill
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Resume._meta.fields]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]

@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProfessionalExperience._meta.fields]

@admin.register(Skill)
class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.fields]