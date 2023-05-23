from django.http import HttpResponse
from django.template import loader
from django.templatetags.static import static
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms

from app1.models import SubjectsAvailable, UserSemester, Schedule

import os


class InputActivity(forms.Form):
    subject_name = forms.CharField(label='Input')
    subject_code = forms.CharField(label='Input')

class InputSemester(forms.Form):
    user_semester = forms.IntegerField(label='Input')

def make_available(input_file, user_semester):
    for line in input_file:
        attribute_array = line.split()
        if '-' in attribute_array:
            continue

        if attribute_array[2] == user_semester:
            subject = SubjectsAvailable.objects.create_subject(attribute_array)
            subject.save()

def home(request):
    return redirect('../schedule/step1/')

def input_semester(request):
    template = loader.get_template('input_semester.html')
    context = {}

    if request.method == 'POST':
        form = InputSemester(request.POST)
        if form.is_valid():
            user_semester = form.cleaned_data['user_semester']
            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, 'static/jadwal22-23.txt')
            input_file = open(file_path, 'r')
            
            make_available(input_file, user_semester)

            return redirect('../step2/')
        else:
            form = input_semester(request.POST)

    return HttpResponse(template.render(context, request))

def input_activity(request):
    template = loader.get_template('input_activity.html')
    data = SubjectsAvailable.objects.all()
    context = {"data": data}

    return HttpResponse(template.render(context, request))
