from django.urls import path
from core.pkgbox.apis.views import GuiaViewSet

urlpatterns = [
    path('pkgbox/apis/', GuiaViewSet.as_view())
]
