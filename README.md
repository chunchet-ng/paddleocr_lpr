# PaddleOCR License Plate Recognition Demo

Welcome to the **License Plate Recognition** demo project, powered by [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)!

This repository contains demo code for recognizing license plates, with detailed workflows and hands-on notebooks. The default environment targets [Paperspace](https://www.paperspace.com/), but a [Google Colab version](https://github.com/chunchet-ng/paddleocr_lpr/tree/colab_archive) is also available.

---

## 🚀 Quick Start on Paperspace

**1. Start a Jupyter notebook in Paperspace.**

**2. Clone this repository:**
```bash
git clone https://github.com/chunchet-ng/paddleocr_lpr.git
```

**3. Enter the project folder:**
```bash
cd paddleocr_lpr
```

**4. Set up the Conda environment:**
```bash
bash conda.sh
```

**5. Refresh your environment:**
- Close all terminals and open a new one.
- Ensure the Conda `base` environment is activated.

**6. Finalize setup:**
```bash
bash setup.sh
```

**7. In Jupyter, select the `paddleocr_lpr` kernel for all notebooks.**

---

## 🗂️ Code Structure

- [`Detection_Evaluation/HMean.ipynb`](./Detection_Evaluation/HMean.ipynb)  
  *Calculate HMean for text detection and spotting tasks (with step-by-step examples).*

- [`Recognition_Evaluation/Acc_Edit_Distance.ipynb`](./Recognition_Evaluation/Acc_Edit_Distance.ipynb)  
  *Compute accuracy and edit distance for text recognition tasks.*

- [`License_Plate_Recognition/CCPD_2019.ipynb`](./License_Plate_Recognition/CCPD_2019.ipynb)  
  *Explore and preprocess the CCPD 2019 dataset for license plate detection and recognition.*

- [`License_Plate_Recognition/EAST_CRNN_LPR.ipynb`](./License_Plate_Recognition/EAST_CRNN_LPR.ipynb)  
  *Apply text detection (EAST), recognition (CRNN), and full license plate detection and recognition on CCPD 2019.*

> [!NOTE] 
> Please run the `CCPD_2019` notebook before starting with `EAST_CRNN_LPR` on your first use.

---

## 📝 What You'll Learn

1. **Text Detection & Spotting Evaluation:**  
   How to calculate HMean with practical examples.

2. **Text Recognition Evaluation:**  
   Methods for computing accuracy, edit distance, and counting correctly recognized words.

3. **Working with CCPD 2019:**  
   - Convert the CCPD 2019 dataset into PaddleOCR format.
   - Fine-tune and evaluate text detection (EAST) and recognition (CRNN) models.
   - Compare pre-trained and fine-tuned models using the provided evaluation scripts.

---

## 📦 Dataset & Dependencies

- **[CCPD 2019 dataset](https://github.com/detectRecog/CCPD):**  
  A large-scale, real-world Chinese city parking dataset for license plate detection and recognition.

- **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR):**  
  Powerful and easy-to-use OCR tools.

---

## 🙏 Acknowledgements

- **[@nwjun](https://github.com/nwjun):**
  Special thanks for improving the notebooks and providing valuable feedback! 💪😇👍

---

## 🤝 Contributing

Pull requests, bug reports, and suggestions are welcome! If you use this code or find it useful, please star the repo and share your results.

---
