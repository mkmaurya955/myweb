from django.conf.urls import url
from . import views

app_name = 'Student'

urlpatterns = [
    url('create/', views.create, name='create'),
    url('detail/', views.detail, name='detail'),
    url('search/', views.search, name='search'),
]
