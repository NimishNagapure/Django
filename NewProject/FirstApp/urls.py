from django.urls import path
from FirstApp import views


urlpatterns = [
    path('emp/',views.employee)
]
