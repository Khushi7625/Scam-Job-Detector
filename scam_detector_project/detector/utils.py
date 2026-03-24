import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, 'model/model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model/vectorizer.pkl'))

def detect_red_flags(text):
    text = text.lower()
    flags = []

    if "fee" in text or "payment" in text or "registration" in text:
        flags.append("Registration or payment mentioned")

    if "guaranteed" in text or "100%" in text:
        flags.append("Guaranteed internship claim")

    if "whatsapp" in text or "telegram" in text:
        flags.append("Informal contact method")

    if "no interview" in text:
        flags.append("No interview process mentioned")

    if "certificate" in text and "training" in text:
        flags.append("Training and certificate focused")

    return flags


def final_prediction(text):
    vector = vectorizer.transform([text])
    ml_result = model.predict(vector)[0]

    flags = detect_red_flags(text)

    if ml_result == "Fake":
        return "Fake", flags
    elif ml_result == "Genuine" and len(flags) >= 2:
        return "Suspicious", flags
    else:
        return "Genuine", flags