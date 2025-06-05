from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import User
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView,
                                    UpdateAPIView, DestroyAPIView)
from .serializers import UserCreateSerializer
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

class IndexView(View):
    def get(self, request):
        return HttpResponse("You're at the crypto app index.")
    
    
# cria objetos
# usa a função create (interna) do CreateAPIView para criar um novo usuário
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    # @transaction.atomic    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        

# lista objetos    
class ListUserView(ListAPIView):
    pass

# recupera objeto específico
class RetrieveUserView(RetrieveAPIView):
    pass

# atualiza objeto
class UpdateUserView(UpdateAPIView):
    pass

# deleta objeto
class DeleteUserView(DestroyAPIView):
    pass