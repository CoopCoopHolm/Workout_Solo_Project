from django.urls import path
from . import views
from .views import DashboardView

urlpatterns = [
    
    path('', views.index),
    path('user/new_user', views.new_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('', views.DashboardView.as_view(), name='dashboard'),
    # path('trip/create_trip', views.create_trip),
    path('user/post', views.post),
    # path('trip/edit_trip_form/<int:trip_id>', views.edit_trip_form),
    # path('trip/update_trip/<int:trip_id>', views.update_trip),
    # path('trip/remove/<int:trip_id>', views.remove),
    # path('trip/details/<int:trip_id>', views.details)
    ]