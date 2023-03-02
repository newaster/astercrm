from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import softwareSerializer,subscriptionSerializer,salesSerializer
from astercrm.models import Subscription,Sales
from django.http.response import JsonResponse

from rest_framework.decorators import api_view

import json

@api_view(['POST'])
def addsoftware(request):
    serializer = softwareSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updatesubscription(request,id):
    try:
        subs = Subscription.objects.get(usage_id=id)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    serializer = subscriptionSerializer(subs, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sales(request):
    tutorials = Sales.objects.all()
    title = request.query_params.get('title', None)
    if title is not None:
        tutorials = tutorials.filter(title__icontains=title)
        
    tutorials_serializer = salesSerializer(tutorials, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)
        



