from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.title



class Talks(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    photo = models.FileField(upload_to='photos')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
