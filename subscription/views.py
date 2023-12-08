from django.shortcuts import render
from .serializers import UserSubSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from users.models import User
from .permissions import SuperUserPermission

# Create your views here.

@api_view(['POST'])
@permission_classes([SuperUserPermission])
def activateUser(request):
    serializer = UserSubSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        User.objects.filter(username=username).update(isActive=True)
        return Response({'message': 'the user has been activated!'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([SuperUserPermission])
def deactivateUser(request):
    serializer = UserSubSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get('username')
        User.objects.filter(username=username).update(isActive=False)
        return Response({'message': 'the user has been deactivated!'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



