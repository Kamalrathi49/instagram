from django.db import models

# Create your models here.

class LoginDetail(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.username
    