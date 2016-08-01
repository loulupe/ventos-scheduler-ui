from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from scheduler.forms import BuildingDataForm,RegistrationDataForm
from scheduler.models import RegDoc,BuildingDoc,buildingdata
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
import csv
import os
from scheduler.utils import read_and_filter_csv,is_whitespace

def index(request):
    return render_to_response('ventos/home.html',context_instance=RequestContext(request))
