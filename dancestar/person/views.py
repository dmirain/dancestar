# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from dancestar.person.forms import ProfileForm, RegistrationForm
from dancestar.person.models import Person

def registration(request):

    if request.method == 'GET':
        form = RegistrationForm(Person())
        return render(request, 'registration.html', {'form': form})

    form = RegistrationForm(Person(), request.POST)
    if form.is_valid():
        return HttpResponse('OK')

    print form.errors
    return render(request, 'registration.html', {'form': form})


@login_required
def profile(request):
    pass


