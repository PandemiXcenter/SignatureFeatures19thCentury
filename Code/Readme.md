This subdirectory contains jupyter notebooks with the python code for the analysis.

Many of the functions used are from a separate github repository under the name "ExcessMortality", developed by the same authors, but kept separately. 
The notebooks here assume that the path to those files are located in a relative path '../../ExcessMortality', i.e. two directories above this 'Code' directory.

Data-collections for specified geographical regions (counties/"amt") were generated based on original raw data, which unfortunately cannot be made publicly available. 
This repository however contains all parts of the analysis, starting with the data-collections available in the "Data" subdirectory. 

The order of notebooks for the analysis is:
* AnalyzeExcessMortality
    
    _Goes through each mortality collection and determines a mortality baseline_

* CollectMortalityCrises

    _Determines mortality crises by identifying continuous periods of excess mortality. Various parameters can be set to determine thresholds for what constitutes a mortality crisis._

* Clustering

    _Carries out the Gaussian Mixture Modelling clustering and generates a number of figures illustrating the results. Also contains part of the sensitivity analysis._

* DetermineGroups

    _Groups together mortality crises that have been determined to be related. Note that visual inspection of plots and validation with various historical sources was used for validating the plausible etiology, in addition to the group-criteria used within the script._

* OverviewPlot 

    _Notebook for creating the overview plot shown in the paper_