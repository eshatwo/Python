from django.db import models
from ..user.models import User, UserManager
import re
import bcrypt
from datetime import datetime

# Create your models here.
class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors['author_len'] = "Author must be at least 3 characters"
        if len(postData['content']) < 10:
            errors['quote_len'] = "Quote must be at least 10 characters"
        return errors

    def account_validator(self, postData):
        if len(postData['first_name']) < 3:
            errors['first_name_len'] = "Please enter a first name"
        if len(postData['last_name']) < 3:
            errors['last_name_len'] = "Please enter a last name"
        if len(postData['email']) < 1:
            errors['email_len'] = "Email is required"
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['email_valid'] = "Email must be in the proper format"
        elif User.objects.filter(email=postData['email']):
            errors['email_taken'] = "This email is already being used"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name='my_quotes')
    users_liked = models.ManyToManyField(User, related_name='my_likes')
    objects = QuoteManager()
