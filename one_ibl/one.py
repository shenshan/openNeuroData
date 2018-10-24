##
from one import OneAbstract
import one_ibl.utils
import one_ibl.params as par
from one_ibl.misc import is_uuid_string, pprint
import numpy as np
import os


class ONE(OneAbstract):

    def __init__(self):
        # Init connection to the database
        self._alyxClient = one_ibl.utils.AlyxClient()
        self._alyxClient.authenticate(username=par.ALYX_LOGIN, password=par.ALYX_PWD)

    def load(self, eid, dataset_types=None, dict_output=False):
        """
        From a Session ID and dataset types, queries Alyx database, downloads the data
        from Globus, and loads into numpy array.

        :param eid: Experiment ID, for IBL this is the UUID of the Session as per Alyx
         database. Could be a full Alyx URL:
         'http://localhost:8000/sessions/698361f6-b7d0-447d-a25d-42afdef7a0da' or only the UUID:
         '698361f6-b7d0-447d-a25d-42afdef7a0da'
        :type eid: str
        :param dataset_types: [None]: Alyx dataset types to be returned.
        :type dataset_types: list
        :param dict_output: [False]: forces the output as dict to provide context.
        :type dict_output: bool
         If None or an empty dataset_type is specified, the output will be a dictionary by default.

        :return: List of numpy arrays matching the size of dataset_types parameter, OR
         a dictionary containing arrays and context data.
        :rtype: list, dict
        """
        # TODO: feature that downloads a list of datasets from a list of sessions,
        # TODO in this case force dictionary output
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
                    print(urlstr)
                    out['local_path'].append(one_ibl.utils.http_download_file(
                        urlstr, username=par.HTTP_DATA_SERVER_LOGIN,
                        password=par.HTTP_DATA_SERVER_PWD))
        # then another loop over files and load them in numpy. If not npy, just pass empty list
        for fil in out['local_path']:  # this is where I miss switch case
            # FIXME: would be nice to implement json read but parameters from matlab RIG
            # FIXME: may be unreadable... Catch exception...
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

    def list(self, table=None, verbose=False):
        """
        Queries the database for a list of 'users' and/or 'dataset-types' and/or 'subjects' fields

        :param table: the table (s) to query among: 'dataset-types','users'
         and 'subjects'; if empty or None assumes all tables
        :type table: str, list
        :param verbose: [False] prints the list in the current window
        :type verbose: bool

        :return: list of names to query, list of full description in json serialized format
        :rtype: list, list
        """
        tlist = ('dataset-types', 'users', 'subjects')
        field = ('name', 'username', 'nickname')
        if not table:
            table = tlist
        if isinstance(table,str):
            table = [table]
        full_out = []
        list_out = []
        for ind, tab in enumerate(tlist):
            if tab in table:
                full_out.append(self._alyxClient.get('/' + tab))
                list_out.append([f[field[ind]] for f in full_out[-1]])
        if verbose:
            pprint(list_out)
        if len(table) == 1:
            return list_out[0], full_out[0]
        else:
            return list_out, full_out

    def search(self, dataset_types=None, users=None, subject='', date_range=None):
        """
        Applies a filter to the sessions (eid) table and returns a list of json dictionaries
         corresponding to sessions.

        :param dataset_types: list of dataset_types
        :type dataset_types: list
        :param users: a list of users
        :type users: list
        :param subject: the subject nickname
        :type subject: str
        :param date_range: list of 2 strings or list of 2 dates that define the range
        :type date_range: list

        :return: list of eids
         list of json dictionaries, each entry corresponding to a matching session
        :rtype: list, list
        """
        # TODO add a lab field in the session table of ALyx to add as a query
        url = '/sessions?'
        # TODO: make sure string inputs don't break the program
        if dataset_types:
            url = url + 'dataset_types=' + ','.join(dataset_types)  # dataset_types query
        if users:
            url = url + '&users=' + ','.join(users)
        if subject:
            url = url + '&subject=' + subject
        if date_range:
            url = url + '&date_range=' + ','.join(date_range)
        # implements the loading itself
        ses = self._alyxClient.get(url)
        return [s['url'] for s in ses], ses
