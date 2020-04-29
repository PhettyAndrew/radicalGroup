from django.shortcuts import render, get_object_or_404
from .models import Info, Subscribe, Building, Plan
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
    return render(request, 'appRadical/about.html')

# def subscribe(request):
#     form = SubscriptionForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponse(form.cleaned_data['email'])
#     return render(request, 'appRadical/index.html', {'form': form})
