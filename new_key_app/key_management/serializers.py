from rest_framework import serializers
from .models import User, Application, ApplicationKey
from rest_framework.validators import UniqueValidator



class UserCredentialsSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "id"]


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'name']


class ApplicationKeySerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)

    class Meta:
        model = ApplicationKey
        fields = '__all__'

