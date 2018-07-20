# library of small functions
import json
import datetime
import re


def isostr2date(isostr):
    return datetime.datetime.strptime(isostr, '%Y-%m-%dT%H:%M:%S.%f')


def date2isostr(adate):
    return datetime.datetime.isoformat(adate)


def pprint(my_dict):
    print(json.dumps(my_dict, indent=4))


def is_uuid_string(string):
    if len(string) != 36:
        return False
    UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    if UUID_PATTERN.match(string):
        return True
    else:
        return False
