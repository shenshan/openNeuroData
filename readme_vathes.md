# How to search session and load data with ONE


## Search eIDs for spectific subjects

1. From the directory openNeuroData run a python instance.

2. Load the ONE module:

```
    from one_ibl.one import ONE
```

3. Search for link to the data of a specific experimental session, such as:

```
eIDs, eInfo = ONE().search(subject='LEW008')
```
The returned eIDs is a list of urls of all sessions for subject 'LEW008':
```
['https://dev.alyx.internationalbrainlab.org/sessions/1119d581-571d-4125-b73c-6eac02e7d948',
 'https://dev.alyx.internationalbrainlab.org/sessions/295e05fb-1e34-40b9-857a-6459b37e1e63',
 'https://dev.alyx.internationalbrainlab.org/sessions/31de813a-8f80-4005-9e41-8f064796ceb8',
 'https://dev.alyx.internationalbrainlab.org/sessions/37df8d9c-ce33-4b08-ac18-7a61d22e9330',
 'https://dev.alyx.internationalbrainlab.org/sessions/5d6ebefd-b78b-412b-a6f5-6ce9904ca5e9',
 'https://dev.alyx.internationalbrainlab.org/sessions/724f7f80-656d-4637-b52e-a3e9aa2941f3',
 'https://dev.alyx.internationalbrainlab.org/sessions/7c122216-8d56-41bf-b373-a24e13cc7f17',
 'https://dev.alyx.internationalbrainlab.org/sessions/8794f030-cbb9-4e15-8ced-44c3870a27a9',
 'https://dev.alyx.internationalbrainlab.org/sessions/af141d06-7e26-4ab1-a0fd-eac6f5674cea',
 'https://dev.alyx.internationalbrainlab.org/sessions/c28eaf8d-2902-4e6e-a1d3-3bb53e685cfa',
 'https://dev.alyx.internationalbrainlab.org/sessions/e55f9677-d6ed-4f03-8134-7074c2c10d52',
 'https://dev.alyx.internationalbrainlab.org/sessions/f286bebb-f835-4fe6-b671-835b3fff63b0']
```
The returned eInfo is a list of information of session and related dataset in each session. For example:

```
{'subject': 'LEW008',
 'users': ['lauren', 'miles'],
 'location': None,
 'procedures': ['Behavior training/tasks'],
 'lab': 'cortexlab',
 'type': 'Experiment',
 'number': 1,
 'parent_session': None,
 'data_dataset_session_related': [{'id': '094bfd3e-269a-4850-b44c-dde47b562051',
   'name': '_ibl_trials.goCue_times.npy',
   'dataset_type': '_ibl_trials.goCue_times',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.goCue_times.094bfd3e-269a-4850-b44c-dde47b562051.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/094bfd3e-269a-4850-b44c-dde47b562051'},
  {'id': '10c95ae7-e6e2-4c1e-aef9-774c3425e4f2',
   'name': '_ibl_trials.repNum.npy',
   'dataset_type': '_ibl_trials.repNum',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.repNum.10c95ae7-e6e2-4c1e-aef9-774c3425e4f2.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/10c95ae7-e6e2-4c1e-aef9-774c3425e4f2'},
  {'id': '1b5088a4-cca0-4402-8164-872ef5ed48c1',
   'name': '_ibl_trials.stimOn_times.npy',
   'dataset_type': '_ibl_trials.stimOn_times',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.stimOn_times.1b5088a4-cca0-4402-8164-872ef5ed48c1.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/1b5088a4-cca0-4402-8164-872ef5ed48c1'},
  {'id': '21f9c3fa-53c4-421d-a929-0cf69197fe49',
   'name': '_ibl_trials.contrastRight.npy',
   'dataset_type': '_ibl_trials.contrastRight',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.contrastRight.21f9c3fa-53c4-421d-a929-0cf69197fe49.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/21f9c3fa-53c4-421d-a929-0cf69197fe49'},
  {'id': '32427e47-e4a1-4bd7-be2c-ea9640cfdc4e',
   'name': '_ibl_trials.included.npy',
   'dataset_type': '_ibl_trials.included',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.included.32427e47-e4a1-4bd7-be2c-ea9640cfdc4e.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/32427e47-e4a1-4bd7-be2c-ea9640cfdc4e'},
  {'id': '4bd1e80f-9e7e-4aa4-a10b-a9c46f2cd802',
   'name': '_ibl_trials.contrastLeft.npy',
   'dataset_type': '_ibl_trials.contrastLeft',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.contrastLeft.4bd1e80f-9e7e-4aa4-a10b-a9c46f2cd802.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/4bd1e80f-9e7e-4aa4-a10b-a9c46f2cd802'},
  {'id': '60eb0798-d724-456a-9f12-37d987f471b3',
   'name': '_ibl_wheel.velocity.npy',
   'dataset_type': '_ibl_wheel.velocity',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_wheel.velocity.60eb0798-d724-456a-9f12-37d987f471b3.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/60eb0798-d724-456a-9f12-37d987f471b3'},
  {'id': '680177f0-be4d-426f-a202-60dcec43e658',
   'name': '_ibl_wheelMoves.type.csv',
   'dataset_type': '_ibl_wheelMoves.type',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_wheelMoves.type.680177f0-be4d-426f-a202-60dcec43e658.csv',
   'data_format': 'csv',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/680177f0-be4d-426f-a202-60dcec43e658'},
  {'id': '742b0f62-4de8-416a-925c-42782328d987',
   'name': '_ibl_wheel.timestamps.npy',
   'dataset_type': '_ibl_wheel.timestamps',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_wheel.timestamps.742b0f62-4de8-416a-925c-42782328d987.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/742b0f62-4de8-416a-925c-42782328d987'},
  {'id': '859c705a-6e1a-4838-bfbe-a339d88ee762',
   'name': '_ibl_trials.intervals.npy',
   'dataset_type': '_ibl_trials.intervals',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.intervals.859c705a-6e1a-4838-bfbe-a339d88ee762.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/859c705a-6e1a-4838-bfbe-a339d88ee762'},
  {'id': 'd4048b62-6f70-497b-bb5e-ed390ae7d350',
   'name': '_ibl_trials.feedback_times.npy',
   'dataset_type': '_ibl_trials.feedback_times',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.feedback_times.d4048b62-6f70-497b-bb5e-ed390ae7d350.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/d4048b62-6f70-497b-bb5e-ed390ae7d350'},
  {'id': 'd7952f71-de3a-47c5-98e9-8978c7950e39',
   'name': '_ibl_trials.feedbackType.npy',
   'dataset_type': '_ibl_trials.feedbackType',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.feedbackType.d7952f71-de3a-47c5-98e9-8978c7950e39.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/d7952f71-de3a-47c5-98e9-8978c7950e39'},
  {'id': 'e978f400-86eb-4aed-a542-eb5a311e7d8d',
   'name': '_ibl_wheel.position.npy',
   'dataset_type': '_ibl_wheel.position',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_wheel.position.e978f400-86eb-4aed-a542-eb5a311e7d8d.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/e978f400-86eb-4aed-a542-eb5a311e7d8d'},
  {'id': 'f19cd1a8-0f16-460f-b543-58337f9eb5d6',
   'name': '_ibl_trials.choice.npy',
   'dataset_type': '_ibl_trials.choice',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.choice.f19cd1a8-0f16-460f-b543-58337f9eb5d6.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/f19cd1a8-0f16-460f-b543-58337f9eb5d6'},
  {'id': 'fe89fe5e-45ff-42cb-a6b5-1a3247054de7',
   'name': '_ibl_trials.response_times.npy',
   'dataset_type': '_ibl_trials.response_times',
   'data_url': 'http://ibl.flatironinstitute.org/cortexlab/Subjects/LEW008/2018-09-06/1/_ibl_trials.response_times.fe89fe5e-45ff-42cb-a6b5-1a3247054de7.npy',
   'data_format': 'npy',
   'url': 'https://dev.alyx.internationalbrainlab.org/datasets/fe89fe5e-45ff-42cb-a6b5-1a3247054de7'}],
 'narrative': 'auto-generated session',
 'start_time': '2018-09-06T15:43:25',
 'end_time': '2018-09-06T16:30:28',
 'url': 'https://dev.alyx.internationalbrainlab.org/sessions/295e05fb-1e34-40b9-857a-6459b37e1e63'}
```

4. Fetch a particular dataset with its name and the eID of the corresponding session. For example,


```
go_cue_times, choices = ONE().load(eIDs[1], dataset_types = ['_ibl_trials.goCue_times', '_ibl_trials.choice'])
```
The returned go_cue_times and choices have the same length.
