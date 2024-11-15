from django.urls import path
from core.pkgbox.views import KsmUno 

urlpatterns = [
    path('pkgbox/', KsmUno.as_view())
]
