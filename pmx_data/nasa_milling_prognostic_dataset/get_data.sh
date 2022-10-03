#!/bin/bash
#Requires kaggle api, see https://github.com/Kaggle/kaggle-api for installation and setup instructions
kaggle datasets download -p datasets --unzip vinayak123tyagi/milling-data-set-prognostic-data
rm -rf datasets/mill
