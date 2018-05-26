# openNeuroData
Neurophysiology badly needs data standardization. A scientist should be able to analyze data collected in any lab, using the same program without changing a single line of code, rather than spending untold hours figuring out new file formats.

Substantial efforts have recently been put into developing neurodata file standards, but they have not been widely adopted. A similar dynamic has occurred before in other domains. Here we propose a simple model for data standardization in neurophysiology, based on lessons learned by the open microscopy environment ([OME](https://www.openmicroscopy.org/)). OME developed a file format, which is hardly ever used. But they also developed a set of loader functions, that allow scientists to load data from multiple native formats using the same code. These functions successfully standardized microscopy data.

Here we propose a set of simple loader functions for neurophysiology data. Data providers can keep data in any format they like. To join the standard, all a provider needs to do is implement these few functions to fetch the data from their server and load it into Python or MATLAB. Users can then load this data with the same code as any other dataset.

## How it works

Each experiment is identified by an `ExperimentID` - a small token that is unique to that particular experiment. An experiment can have  multiple Datasets, which contain the different types of data recorded in the experiment. If a user already has the ExperimentID in the variable `eID` , they can load data for the experiment using a command like:

```
st, sc, cq = ondLoad(ExperimentID, ['spikes.times', 'spikes.clusters', 'clusters.quality'])
```
This command will load three datasets containing the times and cluster assignments 
