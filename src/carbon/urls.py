from django.urls import path
from .views import CarbonView

app_name = "carbon"

urlpatterns = [
    path("", CarbonView.as_view(), name="index"),
]
