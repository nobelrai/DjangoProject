from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('staff/', staffs, name='staffs'),
    path('experience/', experience, name='experience'),
    path('education/', education, name='education'),
    path('skills/', skills, name='skills'),
    path('interests/', interests, name='interests'),
    path('awards/', awards, name='awards'),
    path('home', home, name='home'),
    path('students/', students, name='students'),
    path('<str:name>/', show_name, name='show_name'),
    path('', index, name='index')
]