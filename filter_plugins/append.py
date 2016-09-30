#!/usr/bin/env python


def append(dic, element):
    return [x + element for x in dic]


class FilterModule(object):
    def filters(self):
        return {'append': append}
