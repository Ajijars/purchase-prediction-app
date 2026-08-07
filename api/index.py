from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import os

app = FastAPI(title="Purchase Prediction App")

# Load model and scaler from the root of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

FORM_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Purchase Prediction - AMLIS</title>
    <meta name="description" content="Predict whether a customer will make a purchase based on age and estimated salary using a trained ML model.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 48px 40px;
            width: 100%;
            max-width: 460px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
            animation: slideUp 0.6s ease forwards;
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}

        .badge {{
            display: inline-block;
            background: linear-gradient(90deg, #7c3aed, #4f46e5);
            color: white;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 4px 14px;
            border-radius: 20px;
            margin-bottom: 16px;
        }}

        h1 {{
            font-size: 28px;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 8px;
        }}

        .subtitle {{
            font-size: 14px;
            color: rgba(255,255,255,0.5);
        }}

        .form-group {{
            margin-bottom: 20px;
        }}

        label {{
            display: block;
            font-size: 13px;
            font-weight: 500;
            color: rgba(255,255,255,0.7);
            margin-bottom: 8px;
            letter-spacing: 0.3px;
        }}

        input[type="number"] {{
            width: 100%;
            padding: 14px 18px;
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 12px;
            color: #ffffff;
            font-size: 15px;
            font-family: 'Inter', sans-serif;
            outline: none;
            transition: all 0.3s ease;
        }}

        input[type="number"]:focus {{
            border-color: #7c3aed;
            background: rgba(124,58,237,0.1);
            box-shadow: 0 0 0 3px rgba(124,58,237,0.15);
        }}

        input[type="number"]::placeholder {{ color: rgba(255,255,255,0.3); }}

        button {{
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #7c3aed, #4f46e5);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 15px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 8px;
            position: relative;
            overflow: hidden;
        }}

        button::after {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }}

        button:hover {{ transform: translateY(-2px); box-shadow: 0 10px 30px rgba(124,58,237,0.4); }}
        button:hover::after {{ opacity: 1; }}
        button:active {{ transform: translateY(0); }}

        .result {{
            margin-top: 28px;
            padding: 20px 24px;
            border-radius: 14px;
            text-align: center;
            animation: fadeIn 0.5s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.95); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}

        .yes {{
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.35);
        }}

        .no {{
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid rgba(239, 68, 68, 0.35);
        }}

        .result-label {{
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 6px;
        }}

        .yes .result-label {{ color: #34d399; }}
        .no .result-label {{ color: #f87171; }}

        .result-prob {{
            font-size: 13px;
            color: rgba(255,255,255,0.55);
            font-weight: 400;
        }}

        .divider {{
            height: 1px;
            background: rgba(255,255,255,0.08);
            margin: 28px 0;
        }}

        .footer {{
            text-align: center;
            font-size: 12px;
            color: rgba(255,255,255,0.3);
            margin-top: 28px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <div class="badge">ML Powered</div>
            <h1>Will They Purchase?</h1>
            <p class="subtitle">Enter customer details to get a prediction</p>
        </div>

        <form method="post" action="/predict">
            <div class="form-group">
                <label for="age">Age</label>
                <input type="number" id="age" name="age" placeholder="e.g. 35" min="1" max="100" required>
            </div>
            <div class="form-group">
                <label for="estimated_salary">Estimated Salary (USD)</label>
                <input type="number" id="estimated_salary" name="estimated_salary" placeholder="e.g. 75000" min="0" required>
            </div>
            <button type="submit" id="predict-btn">🔮 Predict Now</button>
        </form>

        {result_block}

        <div class="footer">
            AMLIS Purchase Prediction &mdash; Powered by FastAPI &amp; Scikit-Learn
        </div>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return FORM_HTML.format(result_block="")

@app.post("/predict", response_class=HTMLResponse)
def predict(age: int = Form(...), estimated_salary: float = Form(...)):
    X_new = np.array([[age, estimated_salary]])
    X_new_scaled = scaler.transform(X_new)

    prediction = model.predict(X_new_scaled)[0]
    probability = model.predict_proba(X_new_scaled)[0][1]

    css_class = "yes" if prediction == 1 else "no"
    icon = "✅" if prediction == 1 else "❌"
    text = "Will Purchase" if prediction == 1 else "Will NOT Purchase"

    result_block = f"""
    <div class="divider"></div>
    <div class="result {css_class}">
        <div class="result-label">{icon} {text}</div>
        <div class="result-prob">Purchase probability: <strong>{round(probability * 100, 2)}%</strong></div>
    </div>
    """
    return FORM_HTML.format(result_block=result_block)
