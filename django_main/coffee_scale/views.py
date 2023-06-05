from django.shortcuts import render
from django.http import HttpResponse


def get_dummy_data(request):
    value = 123

    return HttpResponse(value)
