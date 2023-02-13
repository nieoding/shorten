from rest_framework import routers
from . import api
from django.urls.conf import path

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('encode', api.EncodeView.as_view()),
] + router.urls