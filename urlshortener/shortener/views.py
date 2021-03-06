from django.shortcuts import render, redirect
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
        print(uid)
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
