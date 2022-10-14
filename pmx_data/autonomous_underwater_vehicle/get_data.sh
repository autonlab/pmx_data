#!/bin/bash
#This script requires unrar - installation instructions at https://www.tecmint.com/how-to-open-extract-and-create-rar-files-in-linux/
wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/7rp2pmr6mx-1.zip
unzip 7rp2pmr6mx-1.zip
rm 7rp2pmr6mx-1.zip
unrar x Dataset.rar
rm Dataset.rar
mv Dataset datasets

python create_summary_csv.py
