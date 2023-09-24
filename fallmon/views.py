from datetime import datetime
from rest_framework.decorators import api_view
from .models import FallHistory, User, FallType
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from rest_framework.response import Response
from .serializers import FallHistorySerializer, UserSerializer


def get_fall_history(request):
    fall_history_id = request.GET.get('id')
    fall_history = get_object_or_404(FallHistory, pk=fall_history_id)
    serialized_data = FallHistorySerializer(fall_history).data
    return Response(serialized_data, status=200)


def create_fall_history(request):
    user_id = request.GET.get('user_id')
    fall_type_name = request.GET.get('fall_type')
    date_string = request.GET.get('created_at')
    created_at = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    user = get_object_or_404(User, pk=user_id)
    fall_type, fall_type_created = FallType.objects.get_or_create(name=fall_type_name)
    if fall_type_created:
        fall_type.save()
    fall_history, created = FallHistory.objects.get_or_create(user_id=user, created_at=created_at, fall_type=fall_type)
    serialized_data = FallHistorySerializer(fall_history).data
    return Response(serialized_data, status=201)


@api_view(['GET'])
def get_fall_history_by_user(request):
    user_id = request.GET.get('id')
    fall_history_list = FallHistory.objects.filter(user_id=user_id)
    return HttpResponse(serializers.serialize('json', fall_history_list), status=200, content_type="application/json")


@api_view(['GET', 'POST'])
def fall_history_view(request):
    if request.method == 'GET':
        return get_fall_history(request)
    elif request.method == 'POST':
        return create_fall_history(request)


@api_view(['POST'])
def user_view(request):
    user_id = request.GET.get('id')
    pw = request.GET.get('pw')
    user, created = User.objects.get_or_create(id=user_id, pw=pw)
    return Response(UserSerializer(user).data, status=201)
