# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
# from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerialize
from measurement.serializers import SensorMeasurementSerializer
from measurement.serializers import SensorUpdateSerializer
from measurement.serializers import MeasurementAllSerializer


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
