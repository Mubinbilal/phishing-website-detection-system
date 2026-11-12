# 🛡️ Phishing Website Detection System

A machine learning web application that classifies a URL as **phishing (malicious)** or **legitimate (safe)**. The system uses Natural Language Processing (NLP) techniques to extract features from URL text, and serves predictions through a lightweight Flask web interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🔍 Overview

Phishing attacks trick users into visiting fraudulent websites that steal credentials, financial data, and personal information. This project tackles the problem by analysing the **text content of a URL** and predicting whether it is likely to be malicious.

A user simply pastes a URL into the web interface and receives an instant verdict:

- ✅ `THIS IS A HEALTHY WEBSITE`
- 🚨 `THIS IS A PHISHING WEBSITE`

---

## ✨ Features

- **URL-based detection**: no need to visit or load the suspicious page.
- **NLP pipeline**: tokenization, stemming, and bag-of-words vectorization.
- **Multiple models explored**: Logistic Regression and Multinomial Naive Bayes.
- **Exploratory analysis**: word clouds of frequent tokens in good vs. bad URLs.
- **Simple web UI**: built with Flask and HTML templates.
- **Pre-trained models included**: run the app immediately without retraining.

---

## ⚙️ How It Works

```
 URL input
    │
    ▼
 Preprocessing   → strip "http(s)://" and "www."
    │
    ▼
 Tokenization    → RegexpTokenizer (alphabetic tokens only)
    │
    ▼
 Stemming        → SnowballStemmer (English)
    │
    ▼
 Vectorization   → CountVectorizer (bag of words)
    │
    ▼
 Classifier      → Trained ML model
    │
    ▼
 Result          → "good" (safe)  /  "bad" (phishing)
```

---

## 🧰 Tech Stack

| Category        | Tools                                      |
| --------------- | ------------------------------------------ |
| Language        | Python                                     |
| Web Framework   | Flask                                      |
| ML / NLP        | scikit-learn, NLTK                         |
| Data Handling   | pandas, NumPy                              |
| Visualization   | Matplotlib, Seaborn, WordCloud             |
| Model Storage   | Pickle (`.pkl`)                            |

---

## 📁 Project Structure

```
phishing-website-detection-system/
│
├── dataset/                                # Training data (phishing_site_urls.csv)
├── templates/
│   └── index.html                          # Web interface
│
├── app.py                                  # Flask application
├── model.py                                # Model training script (exported from notebook)
├── phishing website detection system .ipynb # Full analysis & training notebook
│
├── phishing.pkl                            # Trained classifier used by the app
├── phishing_mnb.pkl                        # Trained Multinomial Naive Bayes model
├── vectorizer.pkl                          # Fitted CountVectorizer
│
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The model is trained on a labelled URL dataset (`dataset/phishing_site_urls.csv`) containing two columns:

| Column  | Description                                      |
| ------- | ------------------------------------------------ |
| `URL`   | The raw website URL                              |
| `Label` | `good` (legitimate) or `bad` (phishing)          |

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/Mubinbilal/phishing-website-detection-system.git
cd phishing-website-detection-system
```

**2. (Recommended) Create a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install flask scikit-learn nltk pandas numpy matplotlib seaborn wordcloud
```

**4. Download required NLTK data (first run only)**

```python
python -c "import nltk; nltk.download('punkt')"
```

---

## ▶️ Usage

**Run the web application**

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

**Steps:**

1. Paste a URL into the input field.
2. Click the submit button.
3. View the prediction displayed on the page.

> ⚠️ The app currently runs with `debug=True`, which is intended for development only. Disable it before any production deployment.

---

## 🧪 Model Training

All experimentation is documented in the Jupyter notebook `phishing website detection system .ipynb`. The workflow includes:

1. **Data loading & inspection**: shape, null checks, and class distribution.
2. **Text preprocessing**: tokenization → stemming → joined text.
3. **Exploratory analysis**: word clouds for legitimate vs. phishing URLs.
4. **Feature extraction**: `CountVectorizer` (bag of words).
5. **Train/test split**: 80% training, 20% testing.
6. **Model training & evaluation**:
   - Logistic Regression
   - Multinomial Naive Bayes
   - Classification report and confusion matrix

To retrain, open the notebook, run all cells, and re-export the fitted vectorizer and model with `pickle`:

```python
import pickle

pickle.dump(cv, open("vectorizer.pkl", "wb"))
pickle.dump(l_model, open("phishing.pkl", "wb"))
```

---

## ⚠️ Limitations

- Predictions rely **only on URL text**; page content, domain age, WHOIS data, and SSL status are not considered.
- A bag-of-words approach can miss obfuscated or newly crafted phishing patterns.
- Results are probabilistic and should **not** be the sole basis for security decisions.
- Model performance depends on the quality and recency of the training dataset.

---

## 🔮 Future Improvements

- [ ] Add handcrafted URL features (length, special characters, IP-based hosts, subdomain count)
- [ ] Try advanced models (Random Forest, XGBoost, or deep learning)
- [ ] Display prediction confidence scores
- [ ] Add input validation and error handling for malformed URLs
- [ ] Provide a REST API endpoint
- [ ] Containerize with Docker and add deployment instructions
- [ ] Add a `requirements.txt` and unit tests
- [ ] Build a browser extension for real-time protection

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source. Add a license of your choice (e.g., [MIT](https://choosealicense.com/licenses/mit/)) by including a `LICENSE` file in the repository.

---

## 👤 Author

**Mubin Bilal**
GitHub: [@Mubinbilal](https://github.com/Mubinbilal)

---

⭐ If you found this project useful, consider giving it a star!
