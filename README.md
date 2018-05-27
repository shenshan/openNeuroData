# Open Neurophysiology Environment
Neurophysiology badly needs data standardization. A scientist should be able to analyze data collected in any lab, using a single analysis program and without changing a single line of code, rather than spending untold hours figuring out new file formats.

Substantial efforts have recently been put into developing neurodata file standards, but they have not been widely adopted. The same thing has happened before in other scientific fields. Here we propose a simple model for data standardization in neurophysiology, based on lessons learned by the open microscopy environment ([OME](https://www.openmicroscopy.org/)). The OME group developed a file format, which is hardly ever used. But they also developed a set of loader functions, which allow scientists to analyze data in multiple native formats using a single program. These loader functions successfully standardized microscopy data.

Here we propose a set of three simple loader functions for neurophysiology data. To adopt the standard, data providers can use any format they like - all they need to do is implement these three functions to fetch the data from their server and load it into Python or MATLAB. Users can then analyze this data with the same exact code as data from any other provider.

## How it works

By a *data provider* we mean an organization that hosts a set of neurophysiology data on an internet server (for example, the [International Brain Lab](https://www.internationalbrainlab.com/)). The Open Neurophysiology Environment (ONE) provides a way for scientists to analyze data from multiple data providers using the same analysis code. There is no need for the scientist to explicitly download data files or understand their format - this is all handled seamlessly by the ONE framework. The ONE protocol can also be used to access a scientist's own experiments store on their personal computer, but we do not describe this use-case here.

When a user wants to analyze data released by a provider, they first import that provider's loader functions. In python, to analyze IBL data, they would type
```
import one_ibl
```
Because it is up to data providers to maintain the loader functions, all a user needs to do to work with data from a specific provider is import their loader module. To analyze Allen data, they could instead type `import one_allen`. After that, all other analysis code will be the same, regardless of which provider's data they are analyzing.

Every experiment a data provider releases is identified by an *experiment ID* (eID) -- a small token that uniquely identifies a particular experiment. It is up to the data provider to specify the format of their eIDs; however we would recommend using a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). 

### Loading data

If a user already knows the eID of an experiment they are interested in, they can load data for the experiment using a command like:
```
st, sc, cq = oneLoad(eID, ['spikes.times', 'spikes.clusters', 'clusters.quality'])
```
This command will download three datasets containing the times and cluster assignments of all spikes recorded in that experiment, together with a quality measure for each cluster. (In practice, the data will be cached on the user's local machine to avoid redownloading from the internet.)

Many neural data signals are time series, and synchronizing these signals is often challenging. We provide a function to interpolate any required timeseries to an evenly or unevenly-sampled timescale of the user's choice. For example the command:
```
hxy, hth, t = oneLoadTS(eID, ['headTracking.xyPos', 'lfp.raw'], sample_rate=1000)
```
would interpolate head position and lfp to a common 1000 Hz sampling rate. The sample times are returned as `t`.

### Searching for experiments
Finally, a user needs to be able to search the data released by a provider, to obtain the eIDs of experiments they want to analyze. To do so they would run a command like:
```
eIDs, eInfo = oneSearch(lab='CortexLabUCL', subject='hercules', required_data=['spikes.times', 'spikes.clusters','headTracking.xyPos'])
```
This would find the eIDs for all experiments collected in the specified lab for the specified experimental subject, for which all of the required data is present. There will be more metadata options to refine the search (e.g. dates, genotypes, experimenter), and additional metadata on each matching experiment is returned in `eInfo`. However, the existence of dataset types is normally enough to find the data you want. For example, if you want to analyze electrophysiology in a particular behavior task, the experiments you want are exactly those with datasets describing the ephys recordings and that task's parameters.

## Standardization

The key to ONE's standardization is the concept of a "standard dataset type". When a user requests one of these (such as `'spikes.times'`), they are guaranteed that each data provider will return them the same information, organized in the same way - in this case, the times of all extracellularly recorded spikes, measured in seconds relative to experiment start, and returned as a 1-dimensional column vector. It is also guaranteed that any dataset types of the form `*.times` will be measured in seconds relative to experiment start, and that all dataset types beginning with the same word (`spikes.times` and `spikes.clusters`) will have the same number of rows, describing multiple attributes of the same objects.

Not all data can be standardized, since each project will do unique experiments. Data providers can thereform add their own project-specific dataset types, in their own namespace. For example the dataset types `ibl.trials.stimulusContrast` and `ibl.trials.rewardProbabilty` could contain information specific to trials in the IBL task. No other data providers would be required to write loaders for these dataset types, but they would all be required to write loaders for the standard types. A conservative list of standard types and experiment metadata search terms would be maintained centrally.
