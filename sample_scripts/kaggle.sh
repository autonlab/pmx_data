#!/bin/bash
#Requires kaggle api, see https://github.com/Kaggle/kaggle-api for installation and setup instructions
kaggle datasets download -p datasets --unzip shasun/tool-wear-detection-in-cnc-mill
rm datasets/README.txt
rm datasets/test_artifact.jpg
