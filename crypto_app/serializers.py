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
    
    def to_internal_value(self, data):
        int_value = super().to_internal_value(data)
        try:
            # Criptografa dados sensíveis
            if 'userDocument' in int_value:
                int_value['userDocument'] = crypt_service.cryptography(int_value['userDocument'])
            if 'creditCardToken' in int_value:
                int_value['creditCardToken'] = crypt_service.cryptography(int_value['creditCardToken'])
        except Exception as e:
            int_value['userDocument'] = 'Erro de criptografia do serializer'
            int_value['creditCardToken'] = 'Erro de criptografia do serializer'
            print(f"Criptografia: {e}")
        return int_value
    
    # nova instância de objeto usuário
    def create(self, validated_data):
        # Os dados já foram criptografados no método to_internal_value
        # Apenas cria o usuário com os dados validados
        # user = User.objects.create(**validated_data)
        user = User(
            userDocument = validated_data['userDocument'],
            creditCardToken = validated_data['creditCardToken'],
            value = validated_data['value']
        )
        user.save()
        return user
    
    # JSON de saída
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            # Verifica se os campos existem antes de tentar descriptografá-los
            if hasattr(instance, 'userDocument') and instance.userDocument:
                rep['userDocument'] = crypt_service.decryptography(instance.userDocument)
            if hasattr(instance, 'creditCardToken') and instance.creditCardToken:
                rep['creditCardToken'] = crypt_service.decryptography(instance.creditCardToken)
        except Exception as e:
            rep['userDocument'] = 'Erro de descriptografia do serializer'
            rep['creditCardToken'] = 'Erro de descriptografia do serializer'
            print(f"[Descriptografia erro]: {e}")
        return rep
    
    def update(self, instance, validated_data):
        
        userDocument = serializers.CharField()
        creditCardToken = serializers.CharField()
        value = serializers.DecimalField(max_digits=10, decimal_places=2)
        
        instance.userDocument = validated_data.get('userDocument', userDocument)
        instance.creditCardToken = validated_data.get('creditCardToken', creditCardToken)
        instance.value = validated_data.get('value', value)
        instance.save()
        return instance
            
        