#!/bin/bash
#above comment specifies that this script will use bash shell interpreter

#download data zip file from the hosting site using wget
wget https://www.datahostingsite/data123.zip

#unzip the zipfile you downloaded into a local subdirectory called "datasets"
unzip -d datasets data123.zip

#remove the zip file since it is no longer needed
rm data.zip

#if your data is already in a csv format that is easy to ingest, no further steps are needed.

