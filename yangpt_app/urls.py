from django.urls import path
from . import views

app_name = 'yangpt_app'

urlpatterns = [
    path('', views.YanGptLV.as_view(), name='index'),
]
