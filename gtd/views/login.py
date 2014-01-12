from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def LoginFailed(request):
    return render(request,'gtd/login_failed.html')
