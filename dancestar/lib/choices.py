# coding: utf-8
from __future__ import unicode_literals, absolute_import


class OrderedChoices(object):
    """
    Как пользоваться:
    >>> _ = lambda x: x  # gettext-заглушка
    >>> MARITAL_STATUS = OrderedChoices(
    ...     ('FREE', 1, _(u'Free')),
    ...     ('MARRIED', 2, _(u'Marred')),
    ...     ('FREE_BUT_NOT', 4, _(u'Free_but_married')),
    ...     ('MARRIED_BUT_IT_MEANS_NOTHING', 3, _(u'Marred_but_free')),
    ... )
    >>> MARITAL_STATUS.FREE
    1
    >>> MARITAL_STATUS.MARRIED
    2
    >>> MARITAL_STATUS.MARRIED_BUT_IT_MEANS_NOTHING
    3
    >>> MARITAL_STATUS.FREE_BUT_NOT
    4
    >>> sorted(MARITAL_STATUS)
    [(1, u'Free'), (2, u'Marred'), (3, u'Marred_but_free'), (4, u'Free_but_married')]
    >>> list(MARITAL_STATUS)
    [(1, u'Free'), (2, u'Marred'), (4, u'Free_but_married'), (3, u'Marred_but_free')]
    >>> MARITAL_STATUS[1]
    u'Free'
    >>> CHOICES_WITH_SHORTCUTS = OrderedChoices(
    ...     ('FREE', 'free'),
    ...     ('MARRIED', 'mar', 'married'),
    ...     ('FREE_BUT_NOT', 'free_but_not'),
    ...     ('MARRIED_BUT_IT_MEANS_NOTHING', 'mnothing', 'married_but_free'),
    ...     'misanthrope',
    ... )
    >>> CHOICES_WITH_SHORTCUTS.FREE
    'free'
    >>> CHOICES_WITH_SHORTCUTS.MARRIED
    'mar'
    >>> list(CHOICES_WITH_SHORTCUTS)
    [('free', 'free'), ('mar', 'married'), ('free_but_not', 'free_but_not'), ('mnothing', 'married_but_free'), ('misanthrope', 'misanthrope')]
    """
    def __init__(self, *choices):
        self._choices = choices
        self._db_values = {}
        self._text_values = {}
        self._pairs = []

        for attr, db_value, text_value in self._equalize(choices):
            self._db_values[attr] = db_value
            self._text_values[db_value] = text_value
            self._text_values[attr] = text_value
            self._pairs.append((db_value, text_value))

    def __getattr__(self, item):
        if item in self._db_values:
            return self._db_values[item]
        else:
            raise AttributeError(item)

    def __getitem__(self, item):
        return self._text_values[item]

    def __iter__(self):
        return iter(self._pairs)

    def __repr__(self):
        return ("{name}({choices})"
                .format(name=self.__class__.__name__,
                        choices=', '.join(str(c) for c in self._choices)))

    def __deepcopy__(self, memo):
        return self.__class__(*copy.deepcopy(self._choices, memo))

    def _equalize(self, choices):
        for items in choices:
            if isinstance(items, (list, tuple)):
                assert len(items) in range(1, 4), 'RTFM!'
                if len(items) == 1:
                    attr = db = text = items[0]
                elif len(items) == 2:
                    attr, db, text = items[0], items[1], items[1]
                elif len(items) == 3:
                    attr, db, text = items
            else:
                attr = db = text = items

            yield attr, db, text

    def _select_by_name(self, names):
        return [(self._db_values[name], self._text_values[name])
                for name in names]

    def choices(self, include_empty=False, empty_label='--------', select=()):
        _choices = []
        if include_empty:
            _choices.append(('', empty_label))
        if select:
            options = self._select_by_name(select)
        else:
            options = list(self)

        return _choices + options

    def get_key(self, value):
        try:
            return (x[0] for x in self._pairs if x[1] == value).next()
        except StopIteration:
            raise KeyError(value)

    def get_name(self, key):
        db_value = key
        try:
            return (
                attr for attr, _db_value
                in self._db_values.iteritems() if _db_value == db_value
            ).next()
        except StopIteration:
            raise KeyError(db_value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
