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
    ('FEMALE', 'female', 'Женский'),
    ('MALE', 'male', 'Мужской'),
)


AGE_GROUPS = OrderedChoices(
    ('JUVENILE_1', 'juvenile_1', 'Дети 1'),
    ('JUVENILE_2', 'juvenile_2', 'Дети 2'),
    ('JUNIOR_1', 'junior_1', 'Юниоры 1'),
    ('JUNIOR_2', 'junior_2', 'Юниоры 2'),
    ('YOUTH_1', 'youth_1', 'Молодёжь 1'),
    ('YOUTH_2', 'youth_2', 'Молодёжь 2'),
    ('AMATEUR', 'amateur', 'Взрослые'),
    ('PROFESSIONAL', 'professional', 'Профессионалы'),
    ('SENIOR_1', 'senior_1', 'Сеньоры 1'),
    ('SENIOR_2', 'senior_2', 'Сеньоры 2'),
    ('SENIOR_3', 'senior_3', 'Сеньоры 3'),
    ('SENIOR_4', 'senior_4', 'Сеньоры 4'),
)


DISCIPLINES = OrderedChoices(
    ('STANDART', 'standart', 'Стандарт'),
    ('LATIN', 'latin', 'Латина'),
    ('DANCE_10', 'dance_10', '10 танцев'),
    ('DANCE_8', 'dance_8', '8 танцев'),
    ('DANCE_6', 'dance_6', '6 танцев'),
    ('DANCE_5', 'dance_5', '5 танцев'),
    ('DANCE_4', 'dance_4', '4 танца'),
    ('DANCE_3', 'dance_3', '3 танца'),
    ('CONTEMPORARY', 'contemporary', 'Современные направления'),
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
