from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class MainPage(View):
    """Список всех устройств с пагинацией"""
    def get(self, request):
        device = Device.objects.all().order_by('-id')
        paginator = Paginator(device, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginator = page.has_other_pages()

        return render(
            request,
            'alert/main_page.html',
            context={'table': page, 'is_paginated': is_paginator}
        )

    def post(self, request):
        """Включение и отключения устройства, так же в этом месте
        должен быть коннект с настоящим устройством"""
        if 'device_id' in request.POST:
            one_device = Device.objects.get(id=request.POST['device_id'])
            if one_device.activity:
                Device.objects.filter(
                    id=request.POST['device_id']).update(activity=False)
            else:
                Device.objects.filter(
                    id=request.POST['device_id']).update(activity=True)
        # Включение|отключение сразу всех устройств
        elif 'start' in request.POST:
            Device.objects.all().update(activity=request.POST['start'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class SomeDevice(View):
    """Переход на каждое отдельное устройство по id"""
    def get(self, request, id_device):
        device = get_object_or_404(Device, id=id_device)
        return render(
            request,
            'alert/id_device_page.html',
            context={'id_device': id_device, 'device': device}
        )

    def post(self, request, id_device):
        one_device = Device.objects.get(id=id_device)
        if one_device.activity:
            Device.objects.filter(
                id=id_device).update(activity=False)
        else:
            Device.objects.filter(
                id=id_device).update(activity=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeviceView(ListCreateAPIView):
    """Получение спика с информацией устройств,
     добавление новых записей, а так же поиск и фильтры"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['type', 'activity']
    search_fields = [
            'id',
            'type',
            'address',
            'Latitude',
            'Longitude',
            'radius_soundcover',
            'activity'
    ]


class SingleDeviceView(RetrieveUpdateDestroyAPIView):
    """Выбор одного устройства по ID, изменение/удаление"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
