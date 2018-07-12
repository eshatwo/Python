from django.db import models
from ..user.models import User, UserManager
import re
import bcrypt
from datetime import datetime

# Create your models here.
class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title_len'] = "Job title must be at least 3 characters"
        if len(postData['description']) < 10:
            errors['description_len'] = "Description must be at least 10 characters"
        if len(postData['location']) < 1:
            errors['location_len'] = "Please enter a location"
        return errors

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name='my_jobs', null=True)
    users = models.ManyToManyField(User, related_name='jobs')
    objects = JobManager()
