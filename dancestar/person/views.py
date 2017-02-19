# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from dancestar.person.forms import ProfileForm, RegistrationForm

# Create your views here.


def registration(request):
    form = RegistrationForm()
    return HttpResponse(form.as_p())


@login_required
def profile(request):
    pass


