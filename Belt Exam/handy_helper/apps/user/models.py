from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name_len'] = "First name must be at least 2 characters"
        elif not re.match('[A-Za-z]+', postData['first_name']):
            errors['first_name_valid'] = "First name must only have letters"
        if len(postData['last_name']) < 2:
            errors['last_name_len'] = "Last name must be at least 2 characters"
        elif not re.match('[A-Za-z]+', postData['last_name']):
            errors['last_name_valid'] = "Last name must only have letters"
        if len(postData['email']) < 1:
            errors['email_len'] = "Email is required"
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['email_valid'] = "Email must be in the proper format"
        elif User.objects.filter(email=postData['email']):
            errors['email_taken'] = "This email is already being used"
        if len(postData['password']) < 8:
            errors['passowrd_len'] = "Password must be at least 8 characters"
        if postData['pw_confirm'] != postData['password']:
            errors['not_confirm'] = "Passwords must match"
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['no_email'] = "Email is required"
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['email_not_valid'] = "Email must be valid"
        if len(postData['password']) < 1:
            errors['no_pass'] = "Please input a password"
        elif len(postData['password']) < 8:
            errors['short_pass'] = "Incorrect password: less than 8 characters"
        if not User.objects.filter(email=postData['email']):
            errors['email_dne'] = "This email does not exist"
        elif bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()) == False:
            errors['incorrect_pass'] = "Incorrect password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    pw_confirm = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
