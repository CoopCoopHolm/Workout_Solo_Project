from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index),
    path('user/new_user', views.new_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/profile', views.profile),
    path('user/schedule', views.schedule),
    path('user/create_schedule', views.create_schedule),
    path('user/post', views.post),
    path('post/delete/<int:post_id>', views.delete),
    ]