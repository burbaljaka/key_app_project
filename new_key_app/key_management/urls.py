from django.urls import path
from .views import *
# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register('test', ApplicationManagementView, basename='application')


urlpatterns = [
    path('create_key/', AppKeyView.as_view()),
    path('test/', ApplicationManagementView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}))
]

# urlpatterns += router.urls