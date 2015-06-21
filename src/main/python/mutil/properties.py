__author__ = 'Monster'

import json
from mbge import context
def parseAsList(value):
    if value is None:
        return None

    return json.loads("[{}]".format(value))

def getWithControllerPrefix(prefix, property, default=None):
    try:
        key = context.controller.name + ":" + property
        return context.controller.owner[key]
    except KeyError:
        key = prefix + ":" + property
        return context.controller.owner.get(key, default)

