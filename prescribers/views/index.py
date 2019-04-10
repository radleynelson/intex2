from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from drugs import models as dmod
from django.db.models import Sum
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import requests
import json

@login_required(login_url='/account')
@view_function
def process_request(request):

    username = str(request.user.username)
    pageMessage = ''
    showMessage = False

    try:
        pageMessage = request.session['pageMessage']
    except:
        pageMessage = ''

    try:
        showMessage = request.session['showMessage']
    except:
        showMessage = False

    request.session['showMessage'] = False
    request.session['pageMessage'] = ''

    context = {
        # sent to index.html and index.js:
        jscontext('data'): {
            'showMessage': showMessage,
            'pageMessage': pageMessage,
            'user': username
        }
    }

    return request.dmp.render('index.html', context)

@view_function
def prescribers_list(request):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    prescribers = dmod.Prescribers.objects.select_related('overdoses', 'specialties').all().values('id', 'doctorid','fname','lname','gender','overdoses__abbrev','credentials','risk_rank','isoutlier','totalprescriptions','numberofopioidsprescribed','specialties__specialty')

    data = list(prescribers)


    return JsonResponse(data, safe=False)

@view_function
def prescriber(request, id:dmod.Prescribers):
    
    if not request.user.is_authenticated:
        return JsonResponse('You must be authorized to access this data', safe=False)

    queryset = dmod.Prescribers.objects.select_related('specialties','overdoses').filter(id = id.id)
    p1 = queryset.values('gender','opioid_prescriber','risk_rank','isoutlier','overdoses__abbrev','specialties__specialty')
    p2 = queryset.values('id','doctorid','fname','lname','credentials','totalprescriptions','numberofopioidsprescribed')
    drugList = dmod.Triple.objects.select_related('opioids').filter(prescribers = id).values('qty', 'opioids__drugname','opioids__isopioid', 'opioids__id')


    data = list(p1)
    dataLeft=list(p2)
    drugs = list(drugList)

    PrescriberDrugs = {
        'PrescriberData': data,
        'PrescriberDataLeft': dataLeft,
        'drugs': drugs
    }
    

    return JsonResponse(PrescriberDrugs, safe=False)


