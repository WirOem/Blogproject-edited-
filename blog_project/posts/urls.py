from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter #new
from .views import UserViewSet, PostViewSet #new

router=SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('',PostViewSet,basename='posts')
urlpatterns= router.urls