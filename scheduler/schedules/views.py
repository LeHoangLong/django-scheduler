from rest_framework import request, generics, authentication, permissions, response
from schedules import serializers
from schedules import models
from rest_framework import status
import json
from django import views, http

class SchedulesView(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request: request.Request):
        serializer = serializers.ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request, *args, **kwargs):
        queryset = models.Schedule.objects.all()
        serializer = serializers.ScheduleSerializer(queryset, many=True)
        return response.Response(serializer.data)

class TaskView(views.View):
    def __init__(self, **kwargs):
        print('kwargs')
        print(kwargs)
        super().__init__(**kwargs)

    def get(self, request, **kwargs):
        print('execute cron')
        print(kwargs)
        print(request.GET.dict())  
        return http.response.HttpResponse(content='ok',status=200)