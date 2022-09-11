from django.urls import path
from . import views


urlpatterns = [
    path('list-data', views.DataListView.as_view()),
    path('', views.home_page),
]