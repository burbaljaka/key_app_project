from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class PermissionClass(HasAPIKey):
    model = ApplicationKey


class AppKeyView(APIView):

    def post(self, request):
        app_name = request.data['name']
        keys = ApplicationKey.objects.filter(application__name=app_name, revoked=False)
        if len(keys) > 0 :
            return Response('Application {} already has a secret key. Please contact site admin'.format(app_name))
        else:
            application = Application.objects.create(name=request.data.pop('app_name'))
            serializer = ApplicationKeySerializer(data=request.data)
            serializer.is_valid()
            key, secret_key = ApplicationKey.objects.create_key(**serializer.validated_data, application=application)
            return Response('Your application key is: {}'.format(secret_key), status=201)


class ApplicationManagementView(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                GenericViewSet):
    permission_classes = [PermissionClass, ]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = "pk"

    def get_object(self):
        key = self.request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        api_key = ApplicationKey.objects.get_from_key(key)
        return api_key.application