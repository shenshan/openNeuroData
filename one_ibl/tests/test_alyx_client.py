import getpass
from one_ibl.alyx_client import AlyxClient
import one_ibl.utils
import one_ibl.params as par

## Init connection to the database
ALYX_PWD = getpass.getpass('Alyx password ?')
HTTP_DATA_SERVER_PWD = ALYX_PWD # it happens to be the same in this case
ac = AlyxClient()
ac._auth( username = par.ALYX_LOGIN, password= ALYX_PWD)


## Test 1: empty dir, dict mode
dset = ac.get('/datasets/6e1d0a00-d4c8-4de2-b483-53e0751a6933')
url = one_ibl.utils.dataset_record_to_url(dset)
file_name = one_ibl.utils.http_download_file_list(url, username=par.HTTP_DATA_SERVER_LOGIN, password=HTTP_DATA_SERVER_PWD,
                                                  verbose=True, cache_dir=par.CACHE_DIR)

## Test 2: empty dir, list mode
dset = ac.get('/datasets?id=6e1d0a00-d4c8-4de2-b483-53e0751a6933')
url = one_ibl.utils.dataset_record_to_url(dset)
file_name = one_ibl.utils.http_download_file_list(url, username=par.HTTP_DATA_SERVER_LOGIN, password=HTTP_DATA_SERVER_PWD,
                                                  verbose=True, cache_dir=par.CACHE_DIR)

## Test 3: 1 file, 1 empty, dict mode
dset = ac.get('/datasets/b916b777-2630-46fd-a545-09e18befde2e') # return a dict
url = one_ibl.utils.dataset_record_to_url(dset)
file_name = one_ibl.utils.http_download_file_list(url, username=par.HTTP_DATA_SERVER_LOGIN, password=HTTP_DATA_SERVER_PWD,
                                                  verbose=True, cache_dir=par.CACHE_DIR)

## Test 4: 1 file, 1 empty, list mode
dset = ac.get('/datasets?id=b916b777-2630-46fd-a545-09e18befde2e') # return a list of dict
url = one_ibl.utils.dataset_record_to_url(dset)
file_name = one_ibl.utils.http_download_file_list(url, username=par.HTTP_DATA_SERVER_LOGIN, password=HTTP_DATA_SERVER_PWD,
                                                  verbose=True, cache_dir=par.CACHE_DIR)
