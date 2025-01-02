from rest_framework.routers import DefaultRouter
from pkgbox.apis.views import GuiaModelViewSet

router_guia = DefaultRouter()

router_guia.register(prefix='guia', basename='guia', viewset=GuiaModelViewSet)
