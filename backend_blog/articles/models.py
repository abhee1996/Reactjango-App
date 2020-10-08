from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    category=models.CharField(max_length=20, default='')
    content = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)


    def __str__(self):
        return self.title