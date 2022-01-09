from django.contrib import admin
from django.urls import path,include
from authuser import views
from .views import ProjectDelete, ProjectList,ProjectDetail,ProjectCreate, MyProjectList, ProjectUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('home', ProjectList.as_view(),name='home'), 
path('project/<int:pk>',ProjectDetail.as_view(),name='project'),
path('project-create',ProjectCreate.as_view(), name='project-create'),
path('myproject', MyProjectList.as_view(),name='myproject'),
path('project-update/<int:pk>',ProjectUpdate.as_view(),name='project-update'),
path('project-delete/<int:pk>',ProjectDelete.as_view(),name='project-delete'),
path('logout',LogoutView.as_view(next_page='/allusers/login'),name='logout'),
]
