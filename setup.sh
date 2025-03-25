source ~/.bashrc

conda create -n paddleocr_lpr -y python=3.10.0
eval "$(conda shell.bash hook)"
conda activate paddleocr_lpr

dpkg -i setup/cuda-keyring_1.0-1_all.deb
apt-get update

source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate paddleocr_lpr

conda install pytorch==1.12.0 torchvision==0.13.0 -c pytorch -y

echo "export LD_LIBRARY_PATH=/root/miniconda3/envs/paddleocr_lpr/lib/python3.10/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH">>~/.bashrc
source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate paddleocr_lpr

pip install -r requirements.txt

conda install ipykernel -y
python -m ipykernel install --user --name=paddleocr_lpr

TARGET_DIR="./License_Plate_Recognition/PaddleOCR"
if [ ! -d "$TARGET_DIR" ]; then
  echo "Cloning repository into $TARGET_DIR..."
  git clone --single-branch --branch release/2.6 https://github.com/PaddlePaddle/PaddleOCR.git "$TARGET_DIR"
else
  echo "Folder '$TARGET_DIR' already exists. Skipping clone."
fi