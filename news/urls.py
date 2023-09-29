
from django.urls import path
from .import views

urlpatterns = [
    path('/<str:cat>', views.getNews,name="news")
]
