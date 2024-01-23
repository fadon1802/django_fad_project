from django.shortcuts import render
from . import models


def index(request):
    data = models.Main.objects.all()
    content = {'data': data}
    return render(
        request,
        'application/index.html',
        context=content
    )


def demand(request):
    data = models.DemandChart.objects.all()
    content = {'data': data}
    return render(
        request,
        'application/demand.html',
        context=content
    )


def geo(request):
    data = models.GeoChart.objects.all()
    content = {'data': data}
    return render(
        request,
        'application/geo.html',
        context=content
    )


def skills(request):
    data = models.Skills.objects.all()
    content = {'data': data}
    return render(
        request,
        'application/skills.html',
        context=content
    )


def vacancies(request):
    from .parser import Parser
    data = Parser().parse()
    content = {'data': data}
    return render(
        request,
        'application/vacancies.html',
        context=content
    )
