from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        # campos que estarão no response
        fields = '__all__'
        read_only_fields = ['id', 'createdAt', 'updatedAt']
    
    # nova instância de objeto usuário
    def create(self, validated_data):
        user = User(
            userDocument=validated_data['userDocument'],
            creditCardToken=validated_data['creditCardToken'],
            value=validated_data['value']
        )
        user.save()
        return user
        