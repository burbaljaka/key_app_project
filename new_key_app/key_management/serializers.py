from rest_framework import serializers
from .models import *

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'name']


class ApplicationKeySerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)

    class Meta:
        model = ApplicationKey
        fields = '__all__'