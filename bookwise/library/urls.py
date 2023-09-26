from django.urls import path
from .views import add_library, my_libraries, home_library

urlpatterns = [
    path("", my_libraries, name="home_library"),
    path("add/", add_library, name='add_library'),
    path("<int:id>", home_library, name='home_library'),
]