from django.urls import path
from core.views import KsmDos

urlpatterns = [
    path('core/', KsmDos.as_view())
]
