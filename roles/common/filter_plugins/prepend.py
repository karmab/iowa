#!/usr/bin/env python


def prepend(dic, element):
    return [element + x for x in dic]


class FilterModule(object):
    def filters(self):
        return {'prepend': prepend}
