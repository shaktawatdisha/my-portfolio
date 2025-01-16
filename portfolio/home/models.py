from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name
    
# class Project(models.Model):
#     name = models.CharField(max_length=100, help_text="Enter the name of the project")
#     description = models.TextField(help_text="Enter a brief description of the project")
#     link = models.URLField(max_length=200, help_text="Enter the project URL")
#     image = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="Upload an image for the project")
#     technologies = models.CharField(max_length=200, help_text="Enter technologies used, separated by commas")
#     date_created = models.DateField(auto_now_add=True, help_text="The date when the project was created")
#     last_updated = models.DateField(auto_now=True, help_text="The date when the project was last updated")
#     author = models.CharField(max_length=100, help_text="Enter the name of the author or team")

#     def __str__(self):
#         return self.name