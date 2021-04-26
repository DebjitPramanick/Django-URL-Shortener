from django.shortcuts import render
from .models import Url
from django.http import HttpResponse
import json
import uuid

# Create your views here.

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data['url']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
