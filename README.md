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
* It is defining the window that splits the seismic wave to a fixed number of timestamps.
* Creating a proximity/heat feature that defines a value for each time stamp, and marks how much each time stamp is close to the timestamp that marks the start of the seismic wave.
* A deep learning model consists mainly of CNN-1D, Pooling, Dropout, and BatchNormalization layers.
* A post-processing step to focus on the area that contains the predicted seismic event is based on splitting the seismic wave into smaller windows and summing all the predictions in each window. Then, we choose the window with the highest summed predictions.
* We then choose the timestamp that has the highest predicted value in that window.
