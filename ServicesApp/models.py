from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ServiceImages')
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

