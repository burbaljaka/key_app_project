from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserView, basename='users')
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('create_key/', AppKeyView.as_view()),
    path('register_user/', RegisteruserView.as_view()),
    path('test/', ApplicationManagementView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls