from rest_framework import serializers

from authentication.models import User, Tasker

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=16)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nome', 'data_nascimento', 'endereco')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            nome=validated_data['nome'],
            data_nascimento=validated_data['data_nascimento'],
            endereco=validated_data['endereco']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class TaskerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tasker
        fields = ('user', 'tipo_servico', 'telefone')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        tasker, created = Tasker.objects.update_or_create(user=user, **validated_data)
        return tasker