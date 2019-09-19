from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='MainPage'),
    path('device/<int:id_device>/', SomeDevice.as_view(), name='SomeDevice'),
    path('api/device/', DeviceView.as_view()),
    path('api/device/<int:pk>', SingleDeviceView.as_view())
]
