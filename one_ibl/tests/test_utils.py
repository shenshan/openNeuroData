import unittest
import numpy as np
import one_ibl.utils
import one_ibl.params as par


class TestDownloadHTTP(unittest.TestCase):

    def test_download_datasets(self):
        # test downloading a single file
        full_link_to_file = r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018' \
                            r'-05-11/1/cwResponse.choice.8dfae09d-15a4-489b-a440-18517bc6b67a.npy'
        file_name = one_ibl.utils.http_download_file(full_link_to_file, verbose=True,
                                                     username=par.HTTP_DATA_SERVER_LOGIN,
                                                     password=par.HTTP_DATA_SERVER_PWD)
        a = np.load(file_name)
        self.assertTrue(len(a) > 0)

        # test downloading a list of files
        links = [r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018'
                 r'-05-11/1/cwResponse.choice.8dfae09d-15a4-489b-a440-18517bc6b67a.npy',
                 r'http://ibl.flatironinstitute.org/cortexlab/Subjects/MW49/2018'
                 r'-05-11/1/cwResponse.times.63c1ad01-1ae2-47c3-b51b-50488403c24f.npy']
        file_list = one_ibl.utils.http_download_file_list(links, verbose=True,
                                                          username=par.HTTP_DATA_SERVER_LOGIN,
                                                          password=par.HTTP_DATA_SERVER_PWD)
        a = np.load(file_list[0])
        b = np.load(file_list[1])
        self.assertTrue(len(a) > 0)
        self.assertTrue(len(b) > 0)


if __name__ == '__main__':
    unittest.main()
