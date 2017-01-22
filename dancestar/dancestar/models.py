# coding: utf-8
from __future__ import unicode_literals, absolute_import



from django.db import models
from django.contrib.auth.models import AbstractUser


from dancestar.lib.choices import OrderedChoices



TSHIRT_SIZE = OrderedChoices(
    ('XXS', 'xxs', 'XXS'),
    ('XS', 'xs', 'XS'),
    ('S', 's', 'S'),
    ('M', 'm', 'M'),
    ('L', 'l', 'L'),
    ('XL', 'xl', 'XL'),
    ('XXL', 'xxl', 'XXL'),
    ('XXXL', 'xxxl', 'XXXL'),
)


GENDER = OrderedChoices(
    ('MALE', 'male', 'MALE'),
    ('FEMALE', 'female', 'FEMALE'),
)

# AGE_GROUP =



class Person(AbstractUser):

    middle_name = models.CharField(max_length=30, blank=True)

    phone = models.CharField(max_length=100)

    gender = models.CharField(max_length=6, choices=GENDER.choices())
    birthday = models.DateField(null=True)
    # club = models.ForeignKey('Club', null=True)

    chief = models.ForeignKey('Person', null=True)
    partner = models.ForeignKey('Person', null=True)

    is_coach = models.BooleanField(default=True)
    # is_student = models.BooleanField(default=True)

    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)

    age_group = models.CharField(max_length=30, blank=True)
    discipline = models.CharField(max_length=30, blank=True)
    standart_level = models.CharField(max_length=30, blank=True)
    latin_level = models.CharField(max_length=30, blank=True)

    tshirt_size = models.CharField(max_length=4, choices=TSHIRT_SIZE.choices(), default='')


class Couple(models.Model):
    lady = models.ForeignKey('Person', null=True)
    man = models.ForeignKey('Person', null=True)


# class Lesson(models.Model):



# class Club(models.Model):



# class Event(models.Model):



# class Entry(models.Model):

#     couple =
#     author =





















