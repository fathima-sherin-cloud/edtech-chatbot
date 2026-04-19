from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_response
import json
import os
import csv
from datetime import datetime

app = Flask(__name__)
CORS(app)

def log_query(message):
    """Log every query to queries.json for dashboard analytics."""
    log_file = 'queries.json'
    
    categories = {
        "courses": ["course", "python", "web", "data", "cyber", "ui", "ux"],
        "fees": ["fee", "cost", "payment", "emi", "price", "discount"],
        "enrollment": ["enroll", "register", "admission", "batch"],
        "schedule": ["schedule", "time", "timing", "class", "weekend", "weekday"],
        "certificate": ["certificate", "certification"],
        "contact": ["contact", "support", "email", "phone"],
        "greetings": ["hello", "hi", "hey", "good morning", "good evening"],
        "help": ["help"],
    }
    
    category = "other"
    msg_lower = message.lower()
    for cat, keywords in categories.items():
        if any(kw in msg_lower for kw in keywords):
            category = cat
            break
    
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = json.load(f)
    else:
        logs = []
    
    logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "message": message,
        "category": category
    })
    
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)

def load_udemy_data():
    """Load and summarize udemy_courses.csv for dashboard."""
    csv_file = 'udemy_courses.csv'
    if not os.path.exists(csv_file):
        return None
    
    subjects = {}
    paid_count = 0
    free_count = 0
    total_subscribers = 0
    total_courses = 0
    prices = []
    
    with open(csv_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_courses += 1
            subject = row.get('subject', 'Other').strip()
            subjects[subject] = subjects.get(subject, 0) + 1
            
            if row.get('is_paid', '').lower() == 'true':
                paid_count += 1
            else:
                free_count += 1
            
            try:
                subs = int(row.get('num_subscribers', 0))
                total_subscribers += subs
            except:
                pass
            
            try:
                price = float(row.get('price', 0))
                if price > 0:
                    prices.append(price)
            except:
                pass
    
    avg_price = round(sum(prices) / len(prices), 2) if prices else 0
    
    return {
        "total_courses": total_courses,
        "paid_count": paid_count,
        "free_count": free_count,
        "total_subscribers": total_subscribers,
        "avg_price": avg_price,
        "subjects": subjects
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"response": "Invalid request."}), 400
    user_message = data["message"]
    bot_reply = get_response(user_message)
    log_query(user_message)
    return jsonify({"response": bot_reply})

@app.route("/dashboard")
def dashboard():
    log_file = 'queries.json'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = json.load(f)
    else:
        logs = []
    
    total_queries = len(logs)
    
    category_counts = {}
    for log in logs:
        cat = log.get('category', 'other')
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    daily_counts = {}
    for log in logs:
        date = log.get('date', '')
        daily_counts[date] = daily_counts.get(date, 0) + 1
    
    keyword_counts = {}
    for log in logs:
        msg = log.get('message', '').lower().strip()
        keyword_counts[msg] = keyword_counts.get(msg, 0) + 1
    
    top_keywords = sorted(
        keyword_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
    
    udemy = load_udemy_data()
    
    analytics = {
        "total_queries": total_queries,
        "category_counts": category_counts,
        "daily_counts": daily_counts,
        "top_keywords": top_keywords,
        "udemy": udemy
    }
    
    return render_template("dashboard.html", analytics=analytics)

if __name__ == "__main__":
    app.run(debug=True)