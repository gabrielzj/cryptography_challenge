import json
from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .services.crypto import CryptoService
import base64
import json


def index():
    return HttpResponse("index page")

# data = request.data  -> POST
# user, many=True -> GET

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    crypt_service = CryptoService()
    if serializer.is_valid():
        user_document = serializer.validated_data.pop("userDocument")
        user_token = serializer.validated_data.pop("creditCardToken" )
        
        user_document_bytes = str(user_document).encode('utf-8')
        user_token_bytes = str(user_token).encode('utf-8')
        
        encrypted_document = crypt_service.cryptography(user_document_bytes)
        encrypted_token = crypt_service.cryptography(user_token_bytes)
        
        serializer.validated_data['userDocument'] = encrypted_document
        serializer.validated_data['creditCardToken'] = encrypted_token
        
        serializer.save(validated_data=serializer.validated_data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_user(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        # get_object_or_404(queryset)
        serializer = UserSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def update_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    