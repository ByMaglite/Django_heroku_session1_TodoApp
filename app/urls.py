from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('logout', views.signout, name='signout'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('status-todo/<int:id>/<str:status>', views.status_todo, name='status-todo')
]
