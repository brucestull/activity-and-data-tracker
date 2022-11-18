from django.views.generic import ListView

from .models import Activity


class ActivityListView(ListView):
    model = Activity
    template_name = 'activities/activity_list.html'