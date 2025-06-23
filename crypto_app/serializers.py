from rest_framework import serializers
from .models import User
from .services.crypto import CryptoService

crypt_service = CryptoService()

#TODO: ver se no banco estiver em bytes transformar em string primeiro
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # campos que estarão no response
        fields = '__all__'
        read_only_fields = ['id', 'createdAt', 'updatedAt']
    
    # nova instância de objeto usuário
    def create(self, validated_data):
        # Criptografa os dados sensíveis antes de salvar
        user_document = validated_data['userDocument']
        credit_card_token = validated_data['creditCardToken']

    # Aplica a criptografia
        encrypted_document = crypt_service.cryptography(user_document)
        encrypted_token = crypt_service.cryptography(credit_card_token)

    # Cria o usuário com os dados criptografados
        user = User(
            userDocument=encrypted_document,
            creditCardToken=encrypted_token,
            value=validated_data['value']
        )
        user.save()
        return user
    
    # JSON de saída
    def to_representation(self, instance):
        
        rep = super().to_representation(instance)
        try:            
            rep['userDocument'] = crypt_service.decryptography(instance.userDocument)
            rep['creditCardToken'] = crypt_service.decryptography(instance.creditCardToken)
        except Exception as e:
            rep['userDocument'] = 'Erro de descriptografia serializer'
            rep['creditCardToken'] = 'Erro de descriptografia'
            print(f"[Descriptografia erro]: {e}")
        return rep
        