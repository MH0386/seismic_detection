# Seismic Detection Model with CNN

Our project focuses on seismic detection across the Solar System for missions on planets like the Moon or Mars. We developed a deep learning-based solution that processes and filters seismic data, ensuring only scientifically important seismic events are transmitted back to Earth. By reducing the volume of data that needs to be sent, we conserve power and improve efficiency, which is critical for long-duration planetary missions. This solution directly addresses the challenge of power management and data transmission on planetary missions, making seismology missions more sustainable and impactful.

## Our Team

![](Team.jpeg)

## Data

* [Seismic Data](https://kaggle.com/datasets/mh0386/seismic-data)

## Model

* [Quake Detector](https://www.kaggle.com/models/mh0386/quake-detector)

## Solution

Our solution consists of 5 steps:
* Defining the window that splits the seismic wave to a fixed number of timestamps.
* Creating a proximity/heat feature that defines a value for each time stamp, and marks how much each time stamp is close to the timestamp that marks the start of the seismic wave.
* A deep learning model consists mainly of CNN-1D, Pooling, Dropout, and BatchNormalization layers.
* A post-processing step to focus on the area that contains the predicted seismic event is based on splitting the seismic wave into smaller windows and summing all the predictions in each window. Then, we choose the window with the highest summed predictions.
* We then choose the timestamp that has the highest predicted value in that window.

> [!IMPORTANT]  
> Our results are saved in `CSV` file at [results file](results/predictions_results.csv)
> 
> In the `file_name` column, files are named as {**APOLLO_NUMBER**}-{**GRADE_LETTER**}-{**EVENT_ID**}.csv
> **APOLLO_NUMBER** is a number from 2 digits, **GRADE_LETTER** is a letter and **EVENT_ID** is a number from 5 digits
> For the first 10 rows, there is no information about **APOLLO_NUMBER** and **GRADE_LETTER** due to they belong to Mars data so it is just **EVENT_ID**.
