from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect


def demo(request):
    return render(request, 'index.html')
