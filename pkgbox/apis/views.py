from rest_framework.viewsets import ModelViewSet
from pkgbox.models import Guia
from pkgbox.apis.serializers import GuiaSerializer
from pkgbox.apis.permissions import IsAdminOrReadOnly


class GuiaModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GuiaSerializer
    #queryset = Guia.objects.all()
    queryset = Guia.objects.filter(stsguia=1)
    