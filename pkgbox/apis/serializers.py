from rest_framework.serializers import ModelSerializer
from pkgbox.models import Guia

class GuiaSerializer(ModelSerializer):
    class Meta:
        model = Guia
        fields = ['empresa', 'stsguia', 'idguia', 'srcfecha', 'srcnombres', 
                  'srcapelluno', 'srcapelldos', 'srctelefono', 'srcdireccion', 
                  'dstnombres', 'dstapelluno', 'dstapelldos', 'dsttelefono', 
                  'dstdireccion', 'peso', 'stspago', 'precio']

class GuiaSerializerV2(ModelSerializer):
    class Meta:
        model = Guia
        fields = ['empresa', 'idguia', 'srcfecha', 'stsguia', 'regsts', 
                  'fecha_reg', 'fecha_mod']
        