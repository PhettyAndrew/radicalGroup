from django.shortcuts import render, get_object_or_404
from .models import Info, Subscribe, Building, Plan, Team
import random
from .forms import SubscriptionForm, ContactForm, PurchaseForm
from django.http import HttpResponse, HttpResponseRedirect

# mpesa_api imports
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword


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
    }
    return render(request, 'appRadical/building_details.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'appRadical/index.html')
    return render(request, 'appRadical/contact.html', {'form': form})


def purchase(request, purchase_id):
    building = get_object_or_404(Building, pk=purchase_id)
    context = {
        'building': building,
    }
    return HttpResponse(building.cost)


def getAccessToken(request):
    consumer_key = 'rbGmhzzotDBUGqyNdfD4l5LinbJhuoyq'
    consumer_secret = 'qOCY6GDdfBk7vD5I'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request, purchase_id):
    building = get_object_or_404(Building, pk=purchase_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST or None)
        if form.is_valid():
            form.save()
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": building.cost,
                "PartyA": 254+form.cleaned_data['phone_number'],  # replace with your phone number to get stk push
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": 254+form.cleaned_data['phone_number'],  # replace with your phone number to get stk push
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Radical Group",
                "TransactionDesc": "Building Plan Purchase."
            }
            response = requests.post(api_url, json=request, headers=headers)
            return HttpResponse("Success")
    else:
        form = PurchaseForm()
    return render(request, 'appRadical/purchase.html', {'form': form})

# def subscribe(request):
#     form = SubscriptionForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponse(form.cleaned_data['email'])
#     return render(request, 'appRadical/index.html', {'form': form})
