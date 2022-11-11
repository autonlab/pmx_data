#!/bin/bash
#above comment specifies that this script will use bash shell interpreter

#download data zip file from the hosting site using wget
wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/fddp3dvvzr-1.zip

#unzip the zipfile you downloaded into a local subdirectory called "datasets"
unzip fddp3dvvzr-1.zip

#remove the zip file since it is no longer needed
rm fddp3dvvzr-1.zip

#if your data is already in a csv format that is easy to ingest, no further steps are needed.

