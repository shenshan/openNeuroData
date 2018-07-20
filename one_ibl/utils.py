import urllib.request
import os
from pathlib import Path
import one_ibl.params as par
import requests
import json


def http_download_file_list(links_to_file_list, **kwargs):
    """ Get a list of files from the flat Iron from a list of links
   Args (required):
       list_of_links_to_file (list): list of (str) http link to the file
   Optional:
       username = '' authentication for password protected
       password = '' authentication for password protected
       cache_dir = homeDir  directory in which files are cached
       verbose = True  displays status of the Download for large files

   Returns
       filenames (list): the local filename downloaded
    """
    file_names_list = []
    for link_str in links_to_file_list:
       file_names_list.append(http_download_file(link_str, **kwargs))
    return file_names_list


def http_download_file(full_link_to_file, *, clobber=False,
                       username='', password='', cache_dir='', verbose=True):
    """ Get a single file from the flat Iron knowing the link
        Args (required):
            full_link_to_file (str): http link to the file
        Optional:
            clobber = False. If set to False, will not overwrite an existing file with the same name
            username = '' authentication for password protected file server
            password = '' authentication for password protected file server
            cache_dir = homeDir  directory in which files are cached
            verbose = True  displays status of the Download for large files

        Returns
            filename (str): the local filename downloaded
    """
    if not(full_link_to_file):
        return ''

    # default cache directory is the home dir
    if len(cache_dir) == 0:
        cache_dir = str(Path.home()) + os.sep + "Downloads"

    # This is the local file name
    file_name = cache_dir + os.sep + os.path.basename(full_link_to_file)

    # do not overwrite an existing file unless specified
    if not clobber and os.path.exists(file_name):
        return file_name

    # This should be the base url you wanted to access.
    baseurl = os.path.split(full_link_to_file)[0]

    # Create a password manager
    manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    if (len(password) != 0) & (len(username) != 0):
        manager.add_password(None, baseurl, username, password)

    # Create an authentication handler using the password manager
    auth = urllib.request.HTTPBasicAuthHandler(manager)

    # Create an opener that will replace the default urlopen method on further calls
    opener = urllib.request.build_opener(auth)
    urllib.request.install_opener(opener)

    # Open the url and get the length
    u = urllib.request.urlopen(full_link_to_file)
    file_size = int(u.getheader('Content-length'))

    if verbose:
        print("Downloading: %s Bytes: %s" % (file_name, file_size))
    file_size_dl = 0
    block_sz = 8192*64
    f = open(file_name, 'wb')
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        if verbose:
            print(status)
    f.close()

    return file_name


def file_record_to_url(file_records, urls=[]):
    """
    Translate a Json dictionary to an usable http url for downlading files
    :param file_records: dictionary containing a 'data_url' field
    :param urls: a list of strings containing previous data_urls
    :return: urls: a list of strings representing full data urls
    """
    for fr in file_records:
        if fr['data_url'] is not None:
            urls.append(fr['data_url'])
    return urls


def dataset_record_to_url(dataset_record):
    """
    Extracts a list of files urls from a list of dataset queries
    :param dataset_record: list of Json dictionary from a rest request
    :return:a list of strings representing files urls corresponding to the datasets records
    """
    urls = []
    if type(dataset_record) is dict:
        dataset_record = [dataset_record]
    for ds in dataset_record:
        urls = file_record_to_url(ds['file_records'], urls)
    return urls


class AlyxClient:
    _token = ''
    _headers = ''

    def __init__(self):
        self.authenticate()

    def authenticate(self, username=par.ALYX_LOGIN, password=par.ALYX_PWD):
        self._token = requests.post(par.BASE_URL + '/auth-token',
                                    data=dict(username=username, password=password)).json()
        self._headers = {
                'Authorization': 'Token {}'.format(list(self._token.values())[0]),
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }

    def get(self, rest_query):
        rest_query = rest_query.replace(par.BASE_URL, '')
        r = requests.get(par.BASE_URL + rest_query, stream=True, headers=self._headers, data=None)
        if r and r.status_code in (200, 201):
            return json.loads(r.text)
        else:
            raise Exception(r)

    def post(self, rest_query):
        rest_query = rest_query.replace(par.BASE_URL, '')
        r = requests.post(par.BASE_URL + rest_query, stream=True, headers=self._headers, data=None)
        return r
