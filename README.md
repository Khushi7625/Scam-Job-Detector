# 💼 Job Scam Detector

A Machine Learning + Django based web application that detects whether a job posting is **Fake, Genuine, or Suspicious**.

This project combines **Natural Language Processing (NLP)** with a **rule-based system** to identify potential job scams and provide users with real-time insights.

---

## 🚀 Features

- 🔍 Detect job scams using ML model
- ⚠️ Identify red flags (WhatsApp hiring, fees, etc.)
- 📊 Dashboard with visual analytics (Chart.js)
- 🧠 Hybrid approach (ML + Rule-based)
- 🎨 Modern UI (Bootstrap + responsive design)
- 📌 Outputs:
  - Genuine ✅
  - Fake ❌
  - Suspicious ⚠️

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django (Python)
- **Machine Learning:** Scikit-learn (Logistic Regression, TF-IDF)
- **Visualization:** Chart.js
- **Tools:** Pandas, NumPy, Joblib

---

## 🧠 How It Works

1. User enters job description
2. Text is processed using **TF-IDF Vectorizer**
3. Model predicts:
   - Fake / Genuine
4. Rule-based system checks for red flags:
   - Payment requests
   - WhatsApp/Telegram contact
   - Guaranteed offers
5. Final output:
   - Fake / Genuine / Suspicious

---

## 📊 Model Performance

- Accuracy: **~97%**
- Better at detecting Genuine jobs
- Moderate recall for Fake jobs (due to imbalanced dataset)

---

## 📁 Project Structure
scam_detector_project/
│
├── detector/
│ ├── templates/
│ │ └── detector/index.html
│ ├── model/
│ │ ├── model.pkl
│ │ └── vectorizer.pkl
│ ├── views.py
│ ├── forms.py
│ ├── utils.py
│ └── urls.py
│
├── scam_detector_project/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
└── db.sqlite3
