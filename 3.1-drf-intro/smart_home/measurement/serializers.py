from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerialize(serializers.ModelSerializer):
    class Meta():
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta():
        model = Measurement
        fields = ['temperature', 'time']


class MeasurementAllSerializer(serializers.ModelSerializer):
    class Meta():
        model = Measurement
        fields = ['sensor', 'temperature', 'time', 'nullable']


class SensorMeasurementSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta():
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
# TODO: опишите необходимые сериализаторы
