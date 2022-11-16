#!/bin/bash
#Requires kaggle api
#see https://github.com/Kaggle/kaggle-api for installation and setup instructions
#or follow below instructions:

#Ensure you have Python 3 and the package manager pip installed.
#run: pip install kaggle
#sign up for a Kaggle account at https://www.kaggle.com
#go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account)
#select 'Create API Token'.
#This will trigger the download of kaggle.json, a file containing your API credentials. 
#Place this file in the location ~/.kaggle/kaggle.json

kaggle datasets download -p datasets --unzip shasun/tool-wear-detection-in-cnc-mill
rm datasets/README.txt
rm datasets/test_artifact.jpg
