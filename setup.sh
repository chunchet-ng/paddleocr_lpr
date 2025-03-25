source ~/.bashrc

conda create -n tibame -y python=3.10.0
eval "$(conda shell.bash hook)"
conda activate tibame

dpkg -i setup/cuda-keyring_1.0-1_all.deb
apt-get update

source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate tibame

conda install pytorch==1.12.0 torchvision==0.13.0 -c pytorch -y

echo "export LD_LIBRARY_PATH=/root/miniconda3/envs/tibame/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH">>~/.bashrc
source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate tibame

conda install ipykernel -y
python -m ipykernel install --user --name=tibame
