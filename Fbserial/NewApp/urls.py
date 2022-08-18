from django.urls import path
from NewApp import views

urlpatterns = [
    path('detail/<int:pk>',views.student_detail),
    path('list/',views.student_list),
]