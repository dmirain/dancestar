# coding: utf-8
from __future__ import unicode_literals, absolute_import



from django.db import models

# from django.auth.models import User



class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField()
    email =
    phone_number =
    gender

    is_student = models.BooleanField()
    is_coach = models.BooleanField()
    is_chief = models.BooleanField()


    birthday =
    city
    country
    club = models.ForeingKey(Club)
    federation = models.CharField()
    class_standart =
    class_latin =
    age_group

    coach = models.ForeingKey(Person)


class Couple(models.Model):
    man = models.ForeingKey(Person)
    lady = models.ForeingKey(Person)


class Club(models.Model):
    name = models.CharField()
    city
    country
    coach = models.ForeingKey(Person)


class Event(models.Model):
    date_start =
    date_end
    name


# Уроки с шаблонами
class Lesson(models.Model):
    name
    is_group
    is_test
    is_


class PackageTemplate(models.Model):
    name =
    is_all_days


class Package(models.Model):
    template = models.ForeingKey(PackageTemplate)
    event = models.ForeingKey(Event)
    order =


class PackagePrice():
    date_start =
    price =


class Application(models.Model):
    event = models.ForeingKey(Event)
    package = models.ForeingKey(Package)


class ApplicationDays(models.Mode):
    application
    day =


class AplicationLesson(models.Model):
    application
    lesson
















