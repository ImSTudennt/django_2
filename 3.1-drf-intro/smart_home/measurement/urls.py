from django.urls import path
from measurement.views import Post_Sensor, Patch_Sensor, Post_Measurement, GetDetail_Sensor, Check

urlpatterns = [
    path('sensors/', Post_Sensor.as_view()),
    path('sensors/<pk>/', Patch_Sensor.as_view()),
    path('measurements/', Post_Measurement.as_view()),
    path('sensorss/<pk>/', GetDetail_Sensor.as_view()),
    path('main/', Check )
]
