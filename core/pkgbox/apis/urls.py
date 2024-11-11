from django.urls import path
from core.pkgbox.apis.views import GuiaApiView

urlpatterns = [
    path('pkgbox/apis/', GuiaApiView.as_view())
]
