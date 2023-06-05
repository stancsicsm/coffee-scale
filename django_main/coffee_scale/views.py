from django.shortcuts import render
from django.http import HttpResponse

from random import randint


def get_dummy_data(request):
    value = randint(0, 100)

    context = {"value": value}
    return render(request, "index.html", context)


def get_weight_dummy(request):
    value = randint(0, 100)

    return HttpResponse(value)
