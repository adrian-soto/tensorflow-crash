#!/bin/bash


# Create new conda environment
conda create -n tensorflow python=2.7

# Activate environment
source activate tensorflow

# Ensure iPython is installed IN THE ENVIRONMENT
conda install ipython
pip install jupyter (if want to use notebooks)

# Install tensorflow 
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.4.0-py2-none-any.whl

# Test Tensorflow
ipython test_tf.py 

# This tutorial also requires numpy and matplotlib
conda install numpy
conda install matplotlib