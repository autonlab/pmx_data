#!/bin/bash
wget https://f001.backblazeb2.com/file/Backblaze-Hard-Drive-Data/data_2013.zip --no-check-certificate
unzip data_2013.zip
rm data_2013.zip
mv 2013 datasets
