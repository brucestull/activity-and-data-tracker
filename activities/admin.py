from django.contrib import admin

from .models import Activity, ActivityInstance


admin.site.register(Activity)
admin.site.register(ActivityInstance)
