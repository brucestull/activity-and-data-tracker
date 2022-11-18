from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'activities'

urlpatterns = [
    path('', TemplateView.as_view(template_name="activities/home.html"), name='home'),
    path('list/', views.ActivityListView.as_view(), name='list'),
]