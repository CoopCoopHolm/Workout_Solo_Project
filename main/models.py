from django.db import models
import re

from django.db.models.base import ModelState

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$")
# Create your models here.

class UserManager(models.Manager):
    def reg_val(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name must be at least 3 characters'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name must be at least 3 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = 'Email already exists'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = 'Passwords must match'
        if not PASSWORD_REGEX.match(postData['password']):
            errors['password'] = 'Password must be between 8 and 20 characters, contain at least one digit, one uppercase, one lowercase and one special character'
        return errors

class PostManager(models.Manager):
    def post_val(self, postData):
        errors = {}
        if len(postData['post']) < 1:
            errors['destination'] = "You can't post blanks."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.user)

# class Workout(models.Model):
#     destination = models.CharField(max_length=100)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     plan = models.CharField(max_length=100)
#     users_trip = models.ForeignKey(User, related_name='user_trip', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = TripManager()
