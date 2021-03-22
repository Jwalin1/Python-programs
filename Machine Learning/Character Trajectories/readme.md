This repository contains 3 files containing different approaches to classify Character Trajectories data.   <br>
Data contains 3 channels : x_vel, y_vel and force.    <br>
Data is of the form time series.    <br>
Dimension of data : [n_sample, n_channels, time_steps]    <br>

We have 3 channels and times steps have been padded to be of length 182.    <br>
Dimension of data : [n_sample, 3, 182]    <br>


Here are the results:

Simple approaches
1) Kmeans    <br>
  -params : n_centroids * dim_centroid = 20*(3*182) = 10920   <br>
  -adjusted_mutual_info_score for train data : 0.7134   <br>
  -adjusted_mutual_info_score for test data : 0.7225    <br>
  
2) Nearest Centroid   <br>
  -params : n_centroids * dim_centroid = 20*(3*182) = 10920   <br>
  -train accuracy : 83.58   <br>
  -test accuracy : 83.01    <br>
  
3) K Nearest Neighbors    <br>
   -params : 1 (slow performace)    <br>
   -train accuracy : 100.0    <br>
   -test accuracy : 94.78     <br>
   
Neural Networks based   <br>
1) CNN    <br>
  -params : 87500   <br>
  -train accuracy : 99.53   <br>
  -test accuracy : 96.73    <br>
  
2) LSTM   <br>
  -params : 74820   <br>
  -train accuracy : 99.72   <br>
  -test accuracy : 97.28    <br>
