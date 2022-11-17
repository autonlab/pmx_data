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

wget https://hostingsite.com/url/data.rar
unrar x data.rar
rm data.rar

#rm -rf rar
