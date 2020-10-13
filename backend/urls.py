from django.urls import include, path, re_path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
	*router.urls,
]