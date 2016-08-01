from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from scheduler.models import RegDoc,BuildingDoc,buildingdata,VentRate,AirDistConf,SysVentEfficiency
from django.utils.translation import ugettext as _
#Create all your forms here
class BuildingDataForm(forms.Form):
    docfile = forms.FileField(
            label='Select a file for building data',
            help_text='max. 42 megabytes',required=True)
    name = forms.CharField(label = 'FileName',required=True)

    
class RegistrationDataForm(forms.Form):
    name = forms.CharField(label = 'FileName',required=True)
    regdocfile = forms.FileField(
            label='Select a file for registration data',
            help_text='max. 42 megabytes',required=True)
    buildingchoices = forms.ModelChoiceField(queryset=BuildingDoc.objects.all(),empty_label="(Nothing)",to_field_name="id",required=True,label="Related Building Data")

class RegisterScheduleForm(forms.Form):
    registerchoices = forms.ModelChoiceField(
            queryset=RegDoc.objects.all(),
            empty_label="(Nothing)",
            to_field_name="id",
            required=True,
            label="Related Building Data")

class airflowform(forms.Form):
    regid = forms.CharField(label = 'RegId',widget=forms.HiddenInput())
    facility = forms.CharField(label = 'Facility')
    enrollment = forms.CharField(label = 'Enrollment')
    space = forms.CharField(label = 'Space')
    starttime = forms.CharField(label = 'Start Time')
    endtime = forms.CharField(label = 'End Time')
    #VentChoice = forms.ModelChoiceField(
    #        queryset=VentRate.objects.all(),
    #        empty_label="(Nothing)",
    #        to_field_name="id",
    #        label="Related Vent Rate Choice"
    #        )
    EvChoice = forms.ModelChoiceField(
           queryset=SysVentEfficiency.objects.all(),
           empty_label="(Nothing)",
           to_field_name="id",
           label="Related Ev Constant")
    EzChoice = forms.ModelChoiceField(
            queryset=AirDistConf.objects.all(),
            empty_label="(Nothing)",
            to_field_name="id",
            label="Related Ez Constant")

