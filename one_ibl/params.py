try:
    import one_ibl.params_secret as sec
except:
    import json
    class DictWrapper(dict):
        def __getattr__(self, attr):
            return self[attr]

    with open('one_config.json', 'r') as f:
        sec = DictWrapper(json.load(f))

# import one_ibl.params as par

# BASE_URL = "https://alyx.cortexlab.net"
# BASE_URL = "https://alyx-dev.cortexlab.net"
BASE_URL = "https://dev.alyx.internationalbrainlab.org/"

ALYX_LOGIN = 'vathes'
ALYX_PWD = sec.ALYX_PWD

HTTP_DATA_SERVER = r'http://ibl.flatironinstitute.org/cortexlab'
HTTP_DATA_SERVER_LOGIN = 'iblmember'
HTTP_DATA_SERVER_PWD = sec.HTTP_DATA_SERVER_PWD  # password for data server

CACHE_DIR = ''  # if empty it will download in the user download directory
