from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path("addrecruiters/", views.addrecruiters, name='addrecruiters'),
    path("recruiters/", views.recruiters, name='recruiters'),
    path("studentprofile/", views.studentprofile, name='studentprofile'),
    path("studentlist/", views.studentlist, name='studentlist'),
    path("profile/", views.profile, name='profile'),
    path("editrecruiters/", views.editrecruiters, name='editrecruiters'),
]