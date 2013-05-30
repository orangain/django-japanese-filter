# coding: utf-8

from unicodedata import east_asian_width

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="truncatewidth")
@stringfilter
def truncatewidth(value, arg):

    try:
        cut_width = int(arg)
    except ValueError: # Invalid literal for int().
        return value # Fail silently.

    return _truncatewidth(value, cut_width)

def _truncatewidth(value, cut_width, truncate = '...'):
    u"""
    >>> print _truncatewidth(u'aあいう', 3)
    aあ...
    >>> print _truncatewidth(u'あいう', 3)
    あ...
    >>> print _truncatewidth(u'あabc', 3)
    あa...
    >>> print _truncatewidth(u'あa', 3)
    あa
    """

    def width(char):
        if east_asian_width(char) in ('W', 'F', 'A'):
            return 2
        else:
            return 1

    total_width = 0
    for i, char in enumerate(value):
        char_width = width(char)
        total_width += char_width

        if total_width > cut_width:
            return value[:i] + truncate

    return value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
