# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerialize, SensorUpdateSerializer, MeasurementSerializer, SensorMeasurementSerializer, MeasurementAllSerializer


class Post_Sensor(ListCreateAPIView):
    
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialize

class Patch_Sensor(RetrieveUpdateAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer

class Post_Measurement(ListCreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementAllSerializer

class GetDetail_Sensor(RetrieveAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorMeasurementSerializer

def Check(request):
    return HttpResponse('Я здесь')





