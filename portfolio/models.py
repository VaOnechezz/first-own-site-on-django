from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # blank=True значит, что поле необязательно

    def __str__(self):
        return self.title