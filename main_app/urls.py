from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index),
    path('user/new_user', views.new_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/profile', views.profile),
    path('user/update_profile',views.update_profile),
    path('user/schedule', views.schedule),
    path('user/create_schedule', views.create_schedule),
    path('user/post', views.post),
    # path('user/comment', views.comment),
    path('post/deletepst/<int:post_id>', views.deletepst),
    # path('post/deletecmt/<int:comment_id>', views.deletecmt),
    ]