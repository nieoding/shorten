from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.core.cache import cache
from django.conf import settings
from .models import Url
from . import shorten

class EncodeView(APIView):
    def get(self, request):
        class Serializer(serializers.Serializer):
            url = serializers.URLField()
        serializer = Serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        source = data['url']
        item = Url.objects.filter(source=source).first()
        if not item:
            cache_key = 'shortincr'
            cache.add(cache_key, 0, timeout=None)
            seq = cache.incr(cache_key)
            pk = shorten.enbase(seq)
            item = Url.objects.create(pk=pk, source=source)
        return Response({'url': f'{settings.MY_CONFIG["domain"]}/{item.pk}'})
