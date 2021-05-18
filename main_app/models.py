# from main_app.views import dashboard
from django.db import models
import re

from django.db.models.base import ModelState
from django.db.models.fields import BLANK_CHOICE_DASH
# from django.shortcuts import redirect

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
            errors['post'] = "You can't post blanks."
        return errors

class CommentManager(models.Manager):
    def comment_val(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "You gotta comment something."
        return errors

class ProfileManager(models.Manager):
    def pro_val(self, postData):
        errors = {}
        if len(postData['bio']) < 0:
            errors['bio'] = "Your bio can't be that boring."
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
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PostManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.post, self.name)

class UpdateProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    current_weight = models.IntegerField(blank=True)
    goal_weight = models.IntegerField(blank=True)
    objects = ProfileManager()