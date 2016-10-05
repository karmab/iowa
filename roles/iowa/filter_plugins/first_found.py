#!/usr/bin/env python

from jinja2.runtime import Undefined


def first_found(elements):
    return next((e for e in list(elements) if not isinstance(e, Undefined)), Undefined())


class FilterModule(object):
    def filters(self):
        return {'first_found': first_found}
