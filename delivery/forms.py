#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
from models import Delivery


class DeliveryFrom(forms.ModelForm):

    class Meta:
        model = Delivery
        exclude = ("id",)

        widgets = {
            'job_name': widgets.Select(attrs={'class': 'form-control','style': 'width:450px;'}),
            'description': widgets.Textarea(attrs={'class': 'form-control','style': 'width:450px; height:100px'}),
            'deploy_policy': widgets.Select(attrs={'class': 'form-control','style': 'width:450px;'}),
            'source_type': widgets.Select(attrs={'class': 'form-control','style': 'width:450px;'}),
            'source_address': widgets.TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'destination_address': widgets.TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            'shell': widgets.Select(attrs={'class': 'form-control','style': 'width:450px;'}),
        }
