from threading import current_thread
from django.shortcuts import render, redirect
from .models import Comment, UpdateProfile, User, Post
from django.views.generic import ListView, CreateView
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'register.html')


def new_user(request):
    if request.method == 'POST':
        errors = User.objects.reg_val(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hash_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hash_pw,
        )
        request.session['logged_in'] = new_user.id

        return redirect('/user/dashboard')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_in'] = log_user.id
                return redirect('/user/dashboard')
        messages.error(request, 'incorrect email or password')

    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def dashboard(request):
    context = {
        'logged_in': User.objects.get(id=request.session['logged_in']),
        'all_posts': Post.objects.all(),
    }
    return render(request, 'dashboard.html', context)


def post(request):
    if request.method == 'POST':
        errors = Post.objects.post_val(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/dashboard')

        user = User.objects.get(id=request.session['logged_in'])
        Post.objects.create(
            user=user,
            body=request.POST['post'],

        )
        return redirect('/user/dashboard')
    return redirect('/user/dashboard')

# def comment(request):
#     if request.method == 'POST':
#         errors = Comment.objects.comment_val(request.POST)

#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/user/dashboard')

#         user = User.objects.get(id=request.session['logged_in'])
#         Comment.objects.create(
#             user=user,
#             body=request.POST['comment'],

#         )
#         return redirect('/user/dashboard')
#     return redirect('/user/dashboard')


def deletepst(request, post_id):
    delete = Post.objects.get(id=post_id)
    delete.delete()
    return redirect('/user/dashboard')

# def deletecmt(request, comment_id):
#     delete = Comment.objects.get(id=comment_id)
#     delete.delete()
#     return redirect('/user/dashboard')


def profile(request):
    context = {
        'logged_in': User.objects.get(id=request.session['logged_in']),
    }
    return render(request, 'profile.html', context)

def update_profile(request):
    if request.method == 'POST':
        errors = UpdateProfile.objects.prof_val(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        update_profile = UpdateProfile.objects.update(
            bio=request.POST['bio'],
            location=request.POST['location'],
            birth_date=request.POST['birth_date'],
            current_weight=request.POST['current_weight'],
            goal_weight=request.POST['goal_weight'],
        )
        request.session['logged_in'] = new_user.id

        return redirect('/user/profile')
    return redirect('/user/profile')

def schedule(request):
    context = {
        'logged_in': User.objects.get(id=request.session['logged_in']),
    }
    return render(request, 'schedule.html', context)

def create_schedule(request):
    return redirect('/user/dashboard')

class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'


class PostView(CreateView):
    model = Post
    template_name = 'dashboard.html'
    fields = '__all__'
