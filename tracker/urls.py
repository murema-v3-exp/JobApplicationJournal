from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('jobs/', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('application/<int:pk>/update-status/', views.update_status, name='update_status'),
    path('application/<int:pk>/', views.application_detail, name='application_detail'),
]

