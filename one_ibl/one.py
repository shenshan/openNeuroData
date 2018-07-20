##
from one import OneAbstract
import one_ibl.utils
import one_ibl.params as par
from one_ibl.misc import is_uuid_string
import numpy as np
import os


class ONE(OneAbstract):

    def __init__(self):
        # Init connection to the database
        self._alyxClient = one_ibl.utils.AlyxClient()
        self._alyxClient.authenticate(username=par.ALYX_LOGIN, password=par.ALYX_PWD)

    def load(self, eid, dataset_types=None, dict_output=False):
        # if the input as an UUID, add the beginning of URL to it
        if is_uuid_string(eid):
            eid = '/sessions/' + eid
        eid_str = eid[-36:]
        # get session json information as a dictionary from the alyx API
        ses = self._alyxClient.get(eid)
        # if no dataset_type is provided:
        # a) force the output to be a dictionary that provides context to the data
        # b) download all types that have a data url specified
        if not dataset_types:
            dict_output = True
            dataset_types = [d['dataset_type'] for d in ses['data_dataset_session_related']
                             if d['data_url']]
        # loop over each dataset related to the session ID and get list of files urls
        session_dtypes = [d['dataset_type'] for d in ses['data_dataset_session_related']]
        out = {'data': [],
               'id': [],
               'local_path': [],
               'dataset_type': [],
               'url': [],
               'eid': []}
        # this first loop only downloads the file to ease eventual refactoring
        for ind, dt in enumerate(dataset_types):
            for [i, sdt] in enumerate(session_dtypes):
                if sdt == dt:
                    urlstr = ses['data_dataset_session_related'][i]['data_url']
                    out['eid'].append(eid_str)
                    out['url'].append(urlstr)
                    out['id'].append(ses['data_dataset_session_related'][i]['id'])
                    out['dataset_type'].append(dt)
                    out['local_path'].append(one_ibl.utils.http_download_file(
                        urlstr, username=par.HTTP_DATA_SERVER_LOGIN,
                        password=par.HTTP_DATA_SERVER_PWD))
                    # local_file_path.append(fpath)
        # then another loop over files and load them in numpy. If not npy, just pass the filename
        for fil in out['local_path']:  # this is where I miss switch case
                if fil and os.path.splitext(fil)[1] == '.npy':
                    out['data'].append(np.load(file=fil))
                else:
                    out['data'].append(np.array([]))
        if dict_output:
            return out
        # if required, parse the output as a list that matches dataset types provided
        list_out = []
        for dtyp in dataset_types:
            tmp_list = []
            for ind, odtyp in enumerate(out['dataset_type']):
                if odtyp == dtyp:
                    tmp_list.append(out['data'][ind])
            if len(tmp_list) == 1:
                list_out.append(tmp_list[0])
            else:
                list_out.append(tmp_list)
        return list_out

    def list(self):
        print('ls')

    def search(self):
        print('search')
