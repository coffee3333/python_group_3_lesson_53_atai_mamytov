from django import forms
from django.forms import widgets
from webapp.models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['summary', 'description', 'status', 'type']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


