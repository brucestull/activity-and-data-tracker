from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'activities'

urlpatterns = [
    path('', TemplateView.as_view(template_name="activities/home.html"), name='home'),
]