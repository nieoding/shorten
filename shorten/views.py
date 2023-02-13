from django.shortcuts import HttpResponseRedirect
from .models import Url

def detail(request, pk):
    item = Url.objects.get(pk=pk)
    return HttpResponseRedirect(item.source)