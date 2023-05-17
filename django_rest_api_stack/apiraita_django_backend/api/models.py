from django.db import models

# Create your models here.
class APOD(models.Model):
    copyright = models.CharField(max_length=100, null=True, blank = True)
    date = models.DateField(null = True, blank = True)
    explanation = models.TextField()
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title