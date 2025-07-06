import os
import requests
from flask import Flask, render_template, request, send_file, session, jsonify
from flask_session import Session
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
from reportlab.pdfgen import canvas
import tempfile
import time

# Load environment variables
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# -------- Helper Functions --------

def get_summary_from_prompt(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.7
    }

    try:
        response = requests.post("https://api.together.xyz/v1/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["text"].strip()
    except:
        return "(MOCKED) Tasks categorized and summarized successfully."

def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text

def generate_prompt(tasks, action):
    tasks_en = translate_to_english(tasks)
    if action == "detailed":
        return f"""
You are a productivity expert. Carefully analyze the tasks listed below.
Group them into detailed categories like 'Work', 'Urgent', 'Errands', etc.
Provide detailed summaries with bullet points and actionable suggestions.

Tasks:
{tasks_en}
"""
    elif action == "brief":
        return f"""
You are an assistant helping to prioritize tasks. Categorize the tasks into 2-3 groups.
Keep summaries brief and list only the top priority tasks under each category.

Tasks:
{tasks_en}
"""
    else:
        return f"""
You are a productivity assistant. I have a list of tasks.
Group them into logical categories like 'Work', 'Personal', 'Urgent', etc.
Give each group a short summary.

Tasks:
{tasks_en}
"""

def colorize(summary):
    categories = ['Work', 'Personal', 'Urgent', 'Errands', 'Learning']
    for cat in categories:
        summary = summary.replace(cat, f"<span class='tag {cat.lower()}'>{cat}</span>")
    return summary

def save_to_pdf(text):
    path = tempfile.mktemp(".pdf")
    c = canvas.Canvas(path)
    y = 800
    c.setFont("Helvetica", 12)
    for line in text.splitlines():
        c.drawString(50, y, line)
        y -= 20
    c.save()
    return path

# -------- Routes --------

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = ""
    summary = ""
    action_type = ""

    if request.method == "POST":
        tasks = request.form.get("tasks", "").strip()
        action = request.form.get("action", "default")

        if tasks:
            prompt = generate_prompt(tasks, action)
            summary_raw = get_summary_from_prompt(prompt)
            summary = colorize(summary_raw)
            
            # Set the action type for headline
            if action == "detailed":
                action_type = "Detailed Summary"
            elif action == "brief":
                action_type = "Brief & Prioritized"
            else:
                action_type = "Summarize (Default)"

    return render_template("index.html", tasks=tasks, summary=summary, action_type=action_type)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    try:
        translated = GoogleTranslator(source='en', target='bn').translate(text)
        return jsonify({"translated": translated})
    except:
        return jsonify({"translated": text})

@app.route("/download-pdf")
def download_pdf():
    return "No summary to download", 400

if __name__ == "__main__":
    app.run(debug=True)
