from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.pkgbox.models import Guia
from core.pkgbox.apis.serializers import GuiaSerializer

class GuiaApiView(APIView):
    def get(self, request):
        serializer = GuiaSerializer(Guia.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    #def get(self, request):
        # 'regid','idguia','srcfecha','regsts','fecha_reg','fecha_mod'
        #guias = [guia.idguia for guia in Guia.objects.all()]
        #return Response(status=status.HTTP_200_OK, data=guias)
    
    def post(self, request):
        pass
    