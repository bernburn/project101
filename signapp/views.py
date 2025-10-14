from django.shortcuts import render

# Create your views here.
from .models import SignUpRegistration
from .serializer import SignUpRegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register_user(request):
    serializer = SignUpRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_user(request):
    users = SignUpRegistration.objects.all()
    serializer = SignUpRegistrationSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = SignUpRegistration.objects.get(pk=pk)
    except SignUpRegistration.DoesNotExist:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SignUpRegistrationSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SignUpRegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        
        else:
            print("Serializer error", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    