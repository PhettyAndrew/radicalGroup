from django.shortcuts import render, get_object_or_404
from .models import Info, Subscribe, Building, Plan, Team
import random
from .forms import SubscriptionForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    infoBuild = Building.objects.order_by("description")
    infoPlan = Plan.objects.order_by("building")
    context = {
        'infoBuild': infoBuild,
        'infoPlan': infoPlan
    }
    return render(request, 'appRadical/index.html', context)


def about(request):
    infoTeam = Team.objects.order_by("name")
    infoBuild = Building.objects.order_by("description")
    context = {
        'infoTeam': infoTeam,
        'infoBuild': infoBuild
    }
    return render(request, 'appRadical/about.html', context)


def plan(request):
    infoBuild = Building.objects.order_by("description")
    infoPlan = Plan.objects.order_by("building")
    context = {
        'infoBuild': infoBuild
    }
    return render(request, 'appRadical/building.html', context)


def building_details(request, building_id):
    building = get_object_or_404(Building, pk=building_id)
    context = {
        'building': building,
        'plan': plan,
    }
    return render(request, 'appRadical/building_details.html', context)

# def subscribe(request):
#     form = SubscriptionForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponse(form.cleaned_data['email'])
#     return render(request, 'appRadical/index.html', {'form': form})
