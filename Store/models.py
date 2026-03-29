
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
class UserProfile (AbstractUser):
    CHOICES_ROLE = (
    ('candidate', 'Candidate'),
    ('employer', 'Employer'),
)
    role = models.CharField(choices=CHOICES_ROLE,default='employer')
    phone_number = PhoneNumberField()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Job(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    salary = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Resume(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skills = models.TextField()
    experience = models.TextField()

class Application(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
