from rest_framework import serializers
from .models import User
from .services.crypto import CryptoService

crypt_service = CryptoService()

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        # campos que estarão no response
        fields = '__all__'
        read_only_fields = ['id', 'createdAt', 'updatedAt']
    
    # nova instância de objeto usuário
    def create(self, validated_data):
        try:
            validated_data['userDocument'] = crypt_service.cryptography(validated_data['userDocument'])
            validated_data['creditCardToken'] = crypt_service.cryptography(validated_data['creditCardToken'])
        except Exception as e:
            validated_data['userDocument'] = 'Erro de criptografia do serializer'
            validated_data['creditCardToken'] = 'Erro de criptografia do serializer'
            print(f"Criptografia: {e}")
        return User.objects.create(**validated_data)
        
    # JSON de saída
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            # Verifica se os campos existem antes de tentar descriptografá-los
            rep['userDocument'] = crypt_service.decryptography(instance.userDocument)
            rep['creditCardToken'] = crypt_service.decryptography(instance.creditCardToken)
        except Exception as e:
            rep['userDocument'] = 'Erro de descriptografia do serializer'
            rep['creditCardToken'] = 'Erro de descriptografia do serializer'
            print(f"[Descriptografia erro]: {e}")
        return rep
    
    def update(self, instance, validated_data):
        try:
            if 'userDocument' in validated_data:
                validated_data['userDocument'] = crypt_service.cryptography(validated_data['userDocument'])
            
            if 'creditCardToken' in validated_data:
                validated_data['creditCardToken'] = crypt_service.cryptography(validated_data['creditCardToken'])        
        
        except Exception as e:
            if 'userDocument' in validated_data:
                validated_data['userDocument'] = 'Erro de criptografia na atualização'
            
            if 'creditCardToken' in validated_data:
                validated_data['creditCardToken'] = 'Erro de criptografia na atualização'
            
            print(f"[Criptografia update erro]: {e}")
            
        instance.userDocument = validated_data.get('userDocument', instance.userDocument)
        instance.creditCardToken = validated_data.get('creditCardToken', instance.creditCardToken)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance
            
        