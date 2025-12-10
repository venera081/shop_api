from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import ConfirmCode, CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    birthday = serializers.DateField()

class AuthValidateSerializer(UserBaseSerializer):
    pass


class RegisterValidateSerializer(UserBaseSerializer):
    def validate_email(self, email):
        try:
            CustomUser.objects.get(email=email)
        except:
            return email
        raise ValidationError('CustomUser уже существует!')
    
class ConfirmSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        code = attrs.get('code')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError('CustomUser не существует!')

        try:
            confirmation_code = ConfirmCode.objects.get(user=user)
        except ConfirmCode.DoesNotExist:
            raise ValidationError('Код подтверждения не найден!')

        if confirmation_code.code != code:
            raise ValidationError('Неверный код подтверждения!')

        return attrs
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['birthday'] = user.birthday.isoformat() if user.birthday else None
        return token
    
class OuathCodeSerializer(serializers.Serializer):
    code = serializers.CharField()