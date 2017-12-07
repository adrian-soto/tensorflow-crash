#!/bin/bash

echo ""
echo "Creating new conda environment"
conda create -n tensorflow python=2.7

echo ""
echo "Activating environment"
source activate tensorflow

echo ""
echo "Ensuring iPython is installed IN THE ENVIRONMENT"
conda install ipython
pip install jupyter 

echo ""
echo "Install tensorflow"
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.4.0-py2-none-any.whl

echo ""
echo "Testing Tensorflow"
ipython test_tf.py 

echo " Installing numpy and matplotlib in the environment"
conda install numpy
conda install matplotlib

