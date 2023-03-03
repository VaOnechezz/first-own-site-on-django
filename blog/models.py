from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=120)
    url = models.URLField(blank=True)
    date= models.DateField()
    description= models.CharField(max_length=500)

    def __str__(self):
        return self.title
    