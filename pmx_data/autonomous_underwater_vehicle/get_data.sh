#!/bin/bash
#This script requires unrar before it will function
#installation instructions at https://www.tecmint.com/how-to-open-extract-and-create-rar-files-in-linux/
#or, uncomment below lines (including the one at the end of the file)

#--------------- On 64-bit --------------- 
#wget https://www.rarlab.com/rar/rarlinux-x64-612.tar.gz
#tar -zxvf rarlinux-x64-612.tar.gz
#rm rarlinux-x64-612.tar.gz
#export PATH="$(pwd)/rar:$PATH"

#--------------- On 32-bit --------------- 
#wget https://www.rarlab.com/rar/rarlinux-x32-612.tar.gz
#tar -zxvf rarlinux-x32-612.tar.gz
#rm rarlinux-x32-612.tar.gz
#export PATH="$(pwd)/rar:$PATH"

wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/7rp2pmr6mx-1.zip
unzip 7rp2pmr6mx-1.zip
rm 7rp2pmr6mx-1.zip
unrar x Dataset.rar
rm Dataset.rar
mv Dataset datasets

python create_summary_csv.py

#rm -rf rar