__author__ = 'Monster'

import json
def parseAsList(value):
    if value is None:
        return None

    return json.loads("[{}]".format(value))