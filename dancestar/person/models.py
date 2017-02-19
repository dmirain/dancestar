# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser

from dancestar.person.constants import GENDERS, AGE_GROUPS, DISCIPLINES, LEVELS, TSHIRT_SIZES


class Person(AbstractUser):

    middle_name = models.CharField(max_length=30, blank=True)

    phone = models.CharField(max_length=100)

    gender = models.CharField(max_length=6, choices=GENDERS.choices())
    birthday = models.DateField(null=True)
    # club = models.ForeignKey('Club', null=True)

    chief = models.ForeignKey('Person', null=True, related_name='students')
    chief_name = models.CharField(max_length=100)
    partner = models.ForeignKey('Person', null=True, related_name='partner_list')

    is_coach = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=True)

    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)

    age_group = models.CharField(max_length=30, choices=AGE_GROUPS.choices(), blank=True)
    discipline = models.CharField(max_length=30, choices=DISCIPLINES.choices(), blank=True)
    standart_level = models.CharField(max_length=30, choices=LEVELS.choices(), blank=True)
    latin_level = models.CharField(max_length=30, choices=LEVELS.choices(), blank=True)

    tshirt_size = models.CharField(max_length=4, choices=TSHIRT_SIZES.choices())

    federation = models.CharField(max_length=30, blank=True)

    couple_name = models.CharField(max_length=100)

    # Карта лояльности
    # card_number = models.CharField(max_length=50)


class Couple(models.Model):
    lady = models.ForeignKey('Person', null=True, related_name='+')
    man = models.ForeignKey('Person', null=True, related_name='+')



# class Club(models.Model):
#     name = models.CharField()
#     city
#     country
#     coach = models.ForeingKey(Person)


# class Event(models.Model):
#     date_start =
#     date_end
#     name


# # Уроки с шаблонами
# class Lesson(models.Model):
#     name
#     is_group
#     is_test
#     is_


# class PackageTemplate(models.Model):
#     name =
#     is_all_days


# class Package(models.Model):
#     template = models.ForeingKey(PackageTemplate)
#     event = models.ForeingKey(Event)
#     order =


# class PackagePrice():
#     date_start =
#     price =


# class Application(models.Model):
#     event = models.ForeingKey(Event)
#     package = models.ForeingKey(Package)


# class ApplicationDays(models.Mode):
#     application
#     day =


# class AplicationLesson(models.Model):
#     application
#     lesson







