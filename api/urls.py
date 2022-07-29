from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import AvariaViewSet, CarroViewSet, RevendedorViewSet, VisitaViewSet


router = SimpleRouter()
router.register('revendedor', RevendedorViewSet)
router.register('carro', CarroViewSet)
router.register('avaria', AvariaViewSet)
router.register('visita', VisitaViewSet)
