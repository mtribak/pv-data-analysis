# PV Production Data Analysis Prototype
## Introduction
This prototype analyzes PV production data gathered from two solar
power plants in India over a 34-day period. The data consists of
power generation and sensor readings, with each pair of files
having one dataset for power generation and another for sensor readings.
The power generation datasets are gathered at the inverter level,
while the sensor data is gathered at a plant level. The data is available
at the following URL: https://www.kaggle.com/datasets/anikannal/solar-power-generation-data

## Data License
The Kaggle data files used in this prototype are © original authors.

## Approach
The data contains the production curves
of 22 inverters for each solar park. The curves range
from 2020-05-15 00:00 to 2020-06-17 23:45 with a granularity of 15 minutes.

The prototype uses a clustering approach of daily curves
to analyze the PV production data. The clustering aims
to find the outliers or atypical daily production curves
for each inverter. 

The **DBSCAN** algorithm is used for clustering, with the **DTW**
distance between the different curves with a time window of 4. 
DTW allows to remove the alignments that can occur between the different
curves due to the passage of clouds or data transmission errors. The first
results are encouraging, as they have shown an efficiency to easily find
daily curves with missing production ranges or inverters with a different
production than the other inverters of the park.

Information such as the exact location of the two parks
or the technical characteristics of each park (orientation, inclination)
can better describe the data and explain some of the differences
jupyter nbconvert --to html my-notebook.ipynbnoticed in the data. However, these data are not available in this dataset.

## Conclusion
This prototype demonstrates a clustering approach of daily curves
to analyze PV production data gathered from two solar power plants in India.
The results are promising and suggest that the approach can be further
developed to analyze atypical production curves and estimate missing data for inverters.

## Perspectives
The following perspectives can be considered for further development of the prototype:

* Use available weather data to explain atypical production curves.
* Estimate the missing data for some inverters.
* Test other clustering algorithms and compare them with the DBSCAN results.

## References
* [Scikit-learn](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html): Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
* “A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise” Ester, M., H. P. Kriegel, J. Sander, and X. Xu, In Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226–231. 1996
* “Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis” Kruskal, J. Psychometrika, 29, (1964)
* Ratanamahatana Chotirat Ann et Keogh Eamonn : Three myths about dynamic time warping data mining.
In Proceedings of the 2005 SIAM international conference on data mining, pages 506–510. SIAM, 2005.
* Rousseeuw Peter J : Silhouettes : a graphical aid to the interpretation and validation of cluster analysis.
Journal of computational and applied mathematics, 20:53–65, 1987.
* [DTAIDistance](https://dtaidistance.readthedocs.io/en/latest/)
 Meert, Wannes;  Hendrickx, Kilian;  Van Craenendonck, Toon;  Robberechts, Pieter;  Blockeel, Hendrik;  Davis, Jesse
    - Improved compilation for M1/M2, and Py3.7
    - Improved plotting warping paths
    - Improved kmeans clustering for ndim
