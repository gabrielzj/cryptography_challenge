from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import User
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView,
                                    UpdateAPIView, DestroyAPIView)

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the crypto app index.")
    
# cria objetos
class CreateUserView(CreateAPIView):
    pass

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