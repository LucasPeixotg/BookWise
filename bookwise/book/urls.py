from django.urls import path
from .views import add_book, detail_book

urlpatterns = [
    path("add/", add_book, name='add_book'),
    path("<int:id>", detail_book, name='detail_book'),
]