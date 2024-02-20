from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

class AdminResidents(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_residents')
    resident_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_admins')
    assigned_at = models.DateTimeField(auto_now_add=True)
