# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django import forms
from django.contrib.auth.forms import SetPasswordForm

from dancestar.person import constants


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Имя', required=True, max_length=30, strip=True)
    last_name = forms.CharField(label='Фамилия', required=True, max_length=30, strip=True)
    middle_name = forms.CharField(label='Отчество', required=False, max_length=30, strip=True)

    gender = forms.ChoiceField(label='Пол', required=True, choices=constants.GENDERS.choices())
    birthday = forms.DateField(label='Дата рождения', required=False)

    phone = forms.CharField(label='Телефон', required=True, max_length=30, strip=True)

    city = forms.CharField(label='Город', required=False, max_length=30, strip=True)
    country = forms.CharField(label='Страна', required=False, max_length=30, strip=True)

    federation = forms.CharField(label='Общественная организация', required=True, max_length=30, strip=True)

    age_group = forms.ChoiceField(label='Возрастная группа', required=True, choices=constants.AGE_GROUPS.choices())
    discipline = forms.ChoiceField(label='Дисциплина', required=True, choices=constants.DISCIPLINES.choices())
    standart_level = forms.ChoiceField(label='Класс мастерства стандарт', required=True, choices=constants.LEVELS.choices())
    latin_level = forms.ChoiceField(label='Класс мастерства латина', required=True, choices=constants.LEVELS.choices())

    tshirt_size = forms.ChoiceField(label='Размер футболки', required=False, choices=constants.TSHIRT_SIZES.choices())

    chief_name = forms.CharField(label='Ф.И.О. тренера', required=False, max_length=100, strip=True)


class RegistrationForm(ProfileForm):#, SetPasswordForm):
    username = forms.CharField(required=True, max_length=150, strip=True)
