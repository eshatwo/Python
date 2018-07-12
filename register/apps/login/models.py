from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData[first_name]) < 2:
            errors['first_name'] = "First name should have at least 2 characters"
        if len(postData[last_name']) < 2:
            errors['last_name'] = "Last name should have at least 2 characters"
        if EMAIL_REGEX.match(postData['email']) == None:
            errors['invalid_email'] = "Email is not in a valid format"
        if User.objects.filter(email = postData['email']):
            errors['taken_email'] = "That email is already taken"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be 8 characters in length"
        if postData['password'] != postData['confirm_pw']:
            errors['unconfirm_pw'] = "Passwords must match"
        return errors
    def login_validator(self, postData):
        user = User.objects.filter(email = postData['email'])
        errors = {}
        if not user:
            errors['email'] = "This email does not exist"
        if user and not bcrypt.checkpw(postData['password'].encode('utf8'), user[0].password.encode('utf8')):
            errors['password'] = "Password is invalid"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 70)
    password = models.CharField(max_length = 50)
    confirm_pw = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()