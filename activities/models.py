from django.db import models


class Activity(models.Model):
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class ActivityInstance(models.Model):
    activity = models.ForeignKey(
        Activity,
        # `PROTECT` prevents deletion of `Activity` instance if it
        #     is associated with a `ActivityInstance` instance.
        # `CASCADE` allows deletion of `Activity` instance and
        #     also does a cascading deletion of `ActivityInstance`.
        # `RESTRICT` allows deletion of `Activity` only if there
        #     is a cascading deletion of `ActivityInstance`.
        on_delete=models.RESTRICT
    )
    duration = models.IntegerField(default=0, help_text="Duration in minutes")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity.description + " -- "  + str(self.duration) + " minutes -- " + str(self.created_on)