from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=500)
    author=models.CharField(max_length=50)
    content=models.CharField(max_length=3000)


    def __str__(self):
        return self.title + " by " +self.author
