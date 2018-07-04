import requests
from getpass import getpass
import urllib.request
import timeit

BASEURL = "https://alyx.cortexlab.net"
BASEURL = "https://alyx-dev.cortexlab.net"

ALYXLOGIN = 'olivier'
ALYXPWD = getpass()

token = requests.post(BASEURL + '/auth-token',
                      data=dict(username=ALYXLOGIN, password=ALYXPWD)).json()

HEADERS = {
    'Authorization': 'Token {}'.format(list(token.values())[0]),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


REST_QUERY = 'https://alyx-dev.cortexlab.net/sessions'

def get_full():
    r = requests.get(REST_QUERY, stream=True, headers=HEADERS, data=None)
    return r


def get_head():
    r = requests.get(REST_QUERY, headers=HEADERS, data=None)
    print('length: ' + r.headers['content-length'])
    return r


def get_head_2():
    req = urllib.request.Request(REST_QUERY)
    [req.add_header(key, value) for key, value in HEADERS.items()]
    resp = urllib.request.urlopen(req)
    print('length: ' + resp.getheader('Content-length'))




u = timeit.timeit(lambda: get_full(), number=1)
print('full ' , u)
u = timeit.timeit(lambda: get_head(), number=1)
print('head ' , u)
u = timeit.timeit(lambda: get_head_2(), number=1)
print('head2 ' , u)



# full  64.74122404600075
# length: 13605637
# head  70.91917553799976
# length: 13605637
# head2  59.21952764100024
# PyDev console: starting.

