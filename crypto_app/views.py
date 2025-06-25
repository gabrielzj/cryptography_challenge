from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .services.crypto import CryptoService


crypt_service = CryptoService()

def index():
    return HttpResponse("index page")

#TODO: ver de colocar criptografia no serializer
@api_view(['POST'])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        # dados são validados com base nas suas restrições
        if serializer.is_valid():            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_user(request):
    try:
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def update_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        # partial = request.method == 'PATCH'
        if request.method == 'PATCH':
            serializer = UserSerializer(queryset, data=request.data, partial=True)
        elif request.method == 'PUT':
            serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'Usuário não existe'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
        queryset.delete()
        return Response({"User deletado com sucesso"}, status=status.HTTP_202_ACCEPTED)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)