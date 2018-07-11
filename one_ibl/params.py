import one_ibl.params_secret as sec
# import one_ibl.params as par

CONFIG_PATH = '~/.alyx'
TABLE_WIDTH = '{0: <72}'

# BASE_URL = "https://alyx.cortexlab.net"
# BASE_URL = "https://alyx-dev.cortexlab.net"
BASE_URL = "http://localhost:8000/"

ALYX_LOGIN = 'olivier'
ALYX_PWD = sec.ALYX_PWD

GLOBUS_CLIENT_ID = sec.GLOBUS_CLIENT_ID

HTTP_DATA_SERVER = r'http://ibl.flatironinstitute.org/cortexlab/'
HTTP_DATA_SERVER_LOGIN = 'ibl'
HTTP_DATA_SERVER_PWD = sec.HTTP_DATA_SERVER_PWD

CACHE_DIR = ''  # if empty it will download in the download directory
