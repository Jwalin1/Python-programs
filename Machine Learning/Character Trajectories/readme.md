This repository contains 3 files containing different approaches to classify Character Trajectories data.
Data contains 3 channels : x_vel, y_vel and force.
Data is of the form time series.
Dimension of data : [n_sample, n_channels, time_steps]

We have 3 channels and times steps have been padded to be of length 182.
Dimension of data : [n_sample, 3, 182]


Here are the results:

Simple approaches
1) Kmeans
  -params : n_centroids * dim_centroid = 20*(3*182) = 10920
  -adjusted_mutual_info_score for train data : 0.7134
  -adjusted_mutual_info_score for test data : 0.7225
  
2) Nearest Centroid
  -params : n_centroids * dim_centroid = 20*(3*182) = 10920
  -train accuracy : 83.58
  -test accuracy : 83.01
  
3) K Nearest Neighbors
   -params : 1 (slow performace)
   -train accuracy : 100.0
   -test accuracy : 94.78
   
Neural Networks based
1) CNN
  -params : 87500
  -train accuracy : 99.53
  -test accuracy : 96.73
  
2) LSTM
  -params : 74820
  -train accuracy : 99.72
  -test accuracy : 97.28
