# EduBot — Edtech Chatbot

A CLI-inspired edtech query assistant built with Python and Flask.
Students can ask questions about courses, fees, schedules, and 
enrollment through a Coursera-style web interface.

## Tech Stack
- Python 3.14
- Flask 3.1.3
- HTML, CSS, JavaScript
- String Matching (keyword-based NLP)

## Features
- 35+ predefined edtech query responses
- CLI-style commands: help, show-status, clear, exit
- Coursera-inspired split-panel UI
- Typing indicator with response delay
- 33 test cases — all passing

## Setup Instructions
1. Clone the repository
   git clone https://github.com/fathima-sherin-cloud/edtech-chatbot.git

2. Navigate to project folder
   cd edtech-chatbot

3. Install dependencies
   python -m pip install flask flask-cors

4. Run the server
   python app.py

5. Open browser and go to
   http://127.0.0.1:5000

## Project Structure
edtech-chatbot/
├── app.py          → Flask server
├── chatbot.py      → String matching engine
├── responses.py    → Keyword-response dataset
├── templates/
│   └── index.html  → Main UI page
├── static/
│   ├── style.css   → Styling
│   └── script.js   → Frontend logic
├── test_cases.md   → 33 test cases
└── README.md       → Project documentation

## Developer
Fathima Sherin | 23BCAICD038
BCA (AI, CC and DevOps)