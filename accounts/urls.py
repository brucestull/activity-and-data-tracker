from django.urls import path

from accounts.views import SignUpView, UserUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="edit_profile"),
]