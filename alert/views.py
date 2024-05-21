from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Alert

# Create your views here.

@login_required
def create(request):
    alert = Alert()
    alert.content = 'Test'
    alert.user = request.user
    alert.save()
    return HttpResponse('Response')