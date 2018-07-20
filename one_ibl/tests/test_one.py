from one_ibl.one import ONE
import unittest
import numpy as np


class TestDownloadHTTP(unittest.TestCase):

    def setUp(self):
        # Init connection to the database
        self.One = ONE()

    def test_load(self):
        # Test with 3 actual datasets predefined
        myone = self.One
        dataset_types = ['cwStimOn.times', 'cwStimOn.contrastRight', 'cwStimOn.contrastLeft']
        eid = 'http://localhost:8000/sessions/698361f6-b7d0-447d-a25d-42afdef7a0da'
        t, cr, cl = myone.load(eid, dataset_types=dataset_types)
        d = myone.load(eid, dataset_types=dataset_types, dict_output=True)
        self.assertTrue(np.all(0 <= cr) and np.all(cr <= 100))
        self.assertTrue(np.all(0 <= cl) and np.all(cl <= 100))
        self.assertTrue(np.all(d['data'][0] == t))

    def test_load_empty(self):
        # Test with a session that doesn't have any dataset on the Flat Iron
        myone = self.One
        eid = 'http://localhost:8000/sessions/01fc6275-cb5c-418a-87e6-3012214d5fca'
        dataset_types = ['wheel.velocity', 'wheel.timestamps']
        a, b = myone.load(eid, dataset_types=dataset_types)
        self.assertTrue((len(a) == 0) & (len(b) == 0))

    def test_load_from_uuid(self):
        # Test the query with only the UUID string and not the full URL (no data here)
        myone = self.One
        eid = '01fc6275-cb5c-418a-87e6-3012214d5fca'
        dataset_types = ['wheel.velocity', 'wheel.timestamps']
        aa = myone.load(eid, dataset_types=dataset_types)
        self.assertTrue(len(aa) == 2)

    def test_load_all_data_available(self):
        # Test without a dataset list should download everything and output a dictionary
        myone = self.One
        eid = 'http://localhost:8000/sessions/698361f6-b7d0-447d-a25d-42afdef7a0da'
        a = myone.load(eid)
        self.assertTrue(isinstance(a, dict))
        self.assertTrue(len(a['data']) == 14)

    def test_load_datasets_with_same_type(self):
        # Test when the dataset type requested is not unique
        myone = self.One
        dataset_types = ['unknown']
        eid = 'http://localhost:8000/sessions/698361f6-b7d0-447d-a25d-42afdef7a0da'
        a = myone.load(eid, dataset_types=dataset_types, dict_output=True)
        self.assertTrue(len(a['id']) == 5)


if __name__ == '__main__':
    unittest.main()
