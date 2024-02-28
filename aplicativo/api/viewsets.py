from rest_framework import viewsets
from aplicativo.models import Carro
from aplicativo.api import serializers



# class CarrosViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.CarrosSerializer
#     queryset = Carro.objects.all()


from rest_framework import viewsets
from aplicativo.models import Carro
from aplicativo.api import serializers

class CarrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarrosSerializer
    
    def get_queryset(self):
        return Carro.objects.all()
