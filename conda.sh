wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
mv Miniconda3-latest-Linux-x86_64.sh setup/
git config --global user.email "xxx@gmail.com"
git config --global user.name "xxx"

bash setup/Miniconda3-latest-Linux-x86_64.sh -b

#!/bin/bash

# Open the .bashrc file and add the Anaconda path to the PATH variable
echo "export PATH=~/miniconda3/bin:\$PATH" >> ~/.bashrc

# Source the .bashrc file to apply changes
eval "$(cat ~/.bashrc | tail -n +10)"

# Verify the installation by checking the version of conda
conda --version

conda init