import urllib.request
import os
from pathlib import Path


def http_download_file_list(links_to_file_list, **kwargs):
    ''' Get a list of files from the flat Iron from a list of links

        Args (required):
            list_of_links_to_file (list): list of (str) http link to the file
        Optional:
            username = '' authentication for password protected
            password = '' authentication for password protected
            cache_dir = homeDir  directory in which files are cached
            verbose = True  displays status of the Download for large files

        Returns
            filenames (list): the local filename downloaded
    '''
    file_names_list = []
    for link_str in links_to_file_list:
        file_names_list.append(http_download_file(link_str, **kwargs))
    return file_names_list


def http_download_file(full_link_to_file, *,
                           username = '', password = '', cache_dir = '', verbose = True):
    ''' Get a single file from the flat Iron knowing the link

        Args (required):
            full_link_to_file (str): http link to the file
        Optional:
            username = '' authentication for password protected
            password = '' authentication for password protected
            cache_dir = homeDir  directory in which files are cached
            verbose = True  displays status of the Download for large files

        Returns
            filename (str): the local filename downloaded
    '''

    if len(full_link_to_file) == 0: return ''

    # default cache directory is the home dir
    if len(cache_dir) == 0:
        cache_dir = str(Path.home()) +  os.sep + "Downloads"

    # This is the local file name
    file_name = cache_dir + os.sep +   os.path.basename(full_link_to_file)

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

    if verbose: print("Downloading: %s Bytes: %s" % (file_name, file_size))
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
        if verbose: print(status)
    f.close()

    return file_name


def file_record_to_url(file_records, urls=[]):
    for fr in file_records:
        if fr['data_url'] is not None:
            urls.append(fr['data_url'])
    return urls


def dataset_record_to_url(dataset_record):
    urls = []
    if type(dataset_record) is dict: dataset_record = [dataset_record]
    for ds in dataset_record:
        urls = file_record_to_url(ds['file_records'], urls)
    return urls

