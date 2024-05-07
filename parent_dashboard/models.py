from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    progress = models.IntegerField(default=0)
    # Add more fields as needed

    def __str__(self):
        return self.name
