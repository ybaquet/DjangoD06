from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyUsers(User):
    release_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.username