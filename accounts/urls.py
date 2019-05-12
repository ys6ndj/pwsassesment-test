from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello_get_query, name='hello_get_query')
]
