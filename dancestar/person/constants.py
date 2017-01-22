# coding: utf-8
from __future__ import unicode_literals, absolute_import

from dancestar.lib.choices import OrderedChoices


TSHIRT_SIZES = OrderedChoices(
    ('XXS', 'xxs', 'XXS'),
    ('XS', 'xs', 'XS'),
    ('S', 's', 'S'),
    ('M', 'm', 'M'),
    ('L', 'l', 'L'),
    ('XL', 'xl', 'XL'),
    ('XXL', 'xxl', 'XXL'),
    ('XXXL', 'xxxl', 'XXXL'),
)


GENDERS = OrderedChoices(
    ('MALE', 'male', 'MALE'),
    ('FEMALE', 'female', 'FEMALE'),
)


AGE_GROUPS = OrderedChoices(
    ('JUVENILE_1', 'juvenile_1', 'Juvenile 1'),
    ('JUVENILE_2', 'juvenile_2', 'Juvenile 2'),
    ('JUNIOR_1', 'junior_1', 'Junior 1'),
    ('JUNIOR_2', 'junior_2', 'Junior 2'),
    ('YOUTH_1', 'youth_1', 'Youth 1'),
    ('YOUTH_2', 'youth_2', 'Youth 2'),
    ('AMATEUR', 'amateur', 'Amateur'),
    ('PROFESSIONAL', 'professional', 'Professional'),
    ('SENIOR_1', 'senior_1', 'Senior 1'),
    ('SENIOR_2', 'senior_2', 'Senior 2'),
    ('SENIOR_3', 'senior_3', 'Senior 3'),
    ('SENIOR_4', 'senior_4', 'Senior 4'),
)


DISCIPLINES = OrderedChoices(
    ('STANDART', 'standart', 'Standart'),
    ('LATIN', 'latin', 'Latin'),
    ('DANCE_10', 'dance_10', '10 dance'),
    ('DANCE_8', 'dance_8', '8 dance'),
    ('DANCE_6', 'dance_6', '6 dance'),
    ('DANCE_5', 'dance_5', '5 dance'),
    ('DANCE_4', 'dance_4', '4 dance'),
    ('DANCE_3', 'dance_3', '3 dance'),
    ('CONTEMPORARY', 'contemporary', 'Contemporary'),
)


LEVELS = OrderedChoices(
    ('N', 'n', 'N'),
    ('E', 'e', 'E'),
    ('D', 'd', 'D'),
    ('C', 'c', 'C'),
    ('B', 'b', 'B'),
    ('A', 'a', 'A'),
    ('S', 's', 'S'),
    ('M', 'm', 'M'),
)
