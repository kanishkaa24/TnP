from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path("addrecruiters/", views.addrecruiters, name='addrecruiters'),
    path("recruiters/", views.recruiters, name='recruiters'),
    path("studentprofile/", views.studentprofile, name='studentprofile'),
    path("studentlist/", views.studentlist, name='studentlist'),
    path("profile/", views.profile, name='profile'),
    path("editrecruiters2022/", views.editrecruiters2022, name='editrecruiters2022'),
    path("editrecruiters2023/", views.editrecruiters2023, name='editrecruiters2023'),
    path("details/", views.details, name='details'),
    path("list/", views.list, name='list'),
    path("editdetails/", views.editdetails, name='editdetails'),
]