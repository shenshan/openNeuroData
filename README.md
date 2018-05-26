# openNeuroData
Neurophysiology badly needs data standardization. A scientist should be able to analyze data collected in any lab, using the same program without changing a single line of code, rather than spending untold hours figuring out new file formats.

Substantial efforts have recently been put into developing neurodata file standards, but they have not been widely adopted. A similar dynamic has occurred previously in other domains. Here we propose a simple model for data standardization in neurophysiology, based on lessons learned by the open microscopy environment ([OME](https://www.openmicroscopy.org/)). OME developed a file format, which is hardly used. But they also developed a set of loader functions, that allow scientists to load data from multiple native formats using the same code. This successfully standardized microscopy data.

Here we propose a set of simple loader functions for neurophysiology data. Data providers can release data in any form they like, or just leave it on a web page. To join the standard, all they need to do is implement these few functions, and users can load their data with the same code as any other dataset.

## How it works

Each experiment is identified by an `ExperimentID` - a small token that is unique to that particular experiment. Each experiment is associated with multiple Datasets, which contain the different types of data recorded in the experiment. If a user knows the ExperimentID, they can load some of these Datasets using a command like:

```
Datasets = ['spikes.times', 'spikes.clusters', 'clusters.quality']
spikeTimes, spikeClusters, clusterQuality = ondLoad(ExperimentID, Datasets)
```
