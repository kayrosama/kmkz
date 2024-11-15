from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from core.pkgbox.models import Guia
from core.pkgbox.apis.serializers import GuiaSerializer
from core.pkgbox.apis.permissions import IsAdminOrReadOnly

class GuiaModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = GuiaSerializer
    queryset = Guia.objects.all()
    
# Utilizando --> APIView
#
#class GuiaApiView(APIView):
#    def get(self, request):
#        serializer = GuiaSerializer(Guia.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    def post(self, request):
#        serializer = GuiaSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)

# Utilizando --> ViewSet
#class GuiaViewSet(ViewSet):
#    def list(self, request):
#        serializer = GuiaSerializer(Guia.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#    def retrives(self, request, pk: int):
#        guia = GuiaSerializer(Guia.objects.get(pk=pk))
#        return Response(status=status.HTTP_200_OK, data=guia.data)
#
#    def create(self, request):
#        serializer = GuiaSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)

    