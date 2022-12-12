from rest_framework.routers import DefaultRouter
from core.api.views import PostApiViewSet

router_seguimiento = DefaultRouter()

router_seguimiento.register(prefix='seguimientos', basename='seguimiento', viewset=PostApiViewSet)