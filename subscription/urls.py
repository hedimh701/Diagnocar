from django.urls import path
from .views import activateUser, deactivateUser



urlpatterns = [
    path('activate', activateUser),
    path('deactivate', deactivateUser),

]