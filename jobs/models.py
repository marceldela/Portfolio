from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    github = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.summary
