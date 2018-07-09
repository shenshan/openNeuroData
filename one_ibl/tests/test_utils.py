# TODO: create a proper testing layout using unittest

import getpass
import numpy as np
import one_ibl.utils

ISERN = 'ibl'
password = getpass("Flat Iron Password ?")

## test downloading a single file
full_link_to_file = r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018-05-11/1/cwResponse.choice.8dfae09d-15a4-489b-a440-18517bc6b67a.npy'
file_name = one_ibl.utils.http_download_file_flatiron(full_link_to_file, username=username, password=password, verbose=True)
a = np.load(file_name)

## test downloading a list of files
links = [ r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018-05-11/1/cwResponse.choice.8dfae09d-15a4-489b-a440-18517bc6b67a.npy',
    r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018-05-11/1/cwResponse.times.63c1ad01-1ae2-47c3-b51b-50488403c24f.npy']
file_list = one_ibl.utils.http_download_file_list_flatiron(links, username=username, password=password, verbose=True)

a = np.load(file_list[0])
b = np.load(file_list[1])

