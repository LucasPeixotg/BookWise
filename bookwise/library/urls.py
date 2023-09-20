from django.urls import path
from .views import add_library, home_library

urlpatterns = [
    path("", home_library, name="home_library"),
    path("add/", add_library, name='add_library'),
]