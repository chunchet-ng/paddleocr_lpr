# Introduction 
This repo contains the demo code for License Plate Recognition using PaddleOCR.
[Paperspace](https://www.paperspace.com/) is used for this demonstration.

# Paperspace Environment Setup
1.	Start a jupyter notebook on paperspace
2.	Git clone the repo by running "git clone https://github.com/chunchet-ng/paddleocr_lpr.git"
3.	Enter the paddleocr_lpr folder by running "cd paddleocr_lpr"
4.	Run "bash conda.sh"
5.	Close all terminals and open a new one, make sure that conda base environment is activated
6.	Run "bash setup.sh"
7.	Run "conda activate tibame"
8.	Run "pip install -r requirements.txt"
9.	Make sure to select tibame as the kernel for all notebooks

# Code Structure/Explanation
1.	[HMean Calculation for Text Detection & Spotting Tasks](/Detection_Evaluation/HMean.ipynb)
2.	[Accuracy & Edit Distance Calculation for Text Recognition Task](/Recognition_Evaluation/Acc_Edit_Distance.ipynb)
3.	[Data Exploration for the CCPD 2019 dataset](/License_Plate_Recognition/CCPD_2019.ipynb)
4.	[Text Detection, Recognition & Spotting on the CCPD 2019 dataset](/License_Plate_Recognition/EAST_CRNN_LPR.ipynb)

>Do note that you need to run the CCPD_2019 notebook before going into EAST_CRNN_LPR for the first time.

# Takeaways
1.	You will learn how the HMean is calculated for the text detection and text spotting tasks with detailed examples.
2.	You will learn how the accuracy, number of correctly recognized words, and total edit distance are calculated for the text recognition task.
3.	You will learn how to make use of the CCPD 2019, a commonly used license plate recognition dataset. Convert the dataset to PaddleOCR format and fine-tune text detection (EAST) and text recognition (CRNN) methods on it. Then, compare the results of using pre-trained and fine-tuned checkpoints using the evaluation methods mentioned above.

# Credits
1.	[CCPD 2019 dataset](https://github.com/detectRecog/CCPD)
2.	[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
3.  Huge thanks to [@nwjun](https://github.com/nwjun) for making the notebooks better and provide valuable feedbacks to this demo! 💪😇👍
