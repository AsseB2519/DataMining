from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import requests
import json

app = Flask(__name__)
CORS(app)

def send_reply_to_talkjs(response_from_dialog):
    url = f"https://api.talkjs.com/v1/tuNjUD9D/conversations/3e5b86cb367a6b8c0689/messages"
    headers = {
        'Authorization': 'Bearer sk_test_Zppk6f56De1RluS70qxCEOeG54sK4wVW',
        'Content-Type': 'application/json'
    }
    data = [{
        "text": response_from_dialog,
        "sender": "2",
        "type": "system"
    }]
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() 
        print(f"Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/webhooks/talkjs', methods=['POST'])
def chatbotReplay():
    incoming_data = request.json
    sender_id = incoming_data['data']['message']['senderId']
    sender_message = incoming_data['data']['message']['text']
    

    if sender_id != "2":  
        response_text = "Hello, I am a chatbot. How can I help you?"
        send_reply_to_talkjs(response_text)
        return jsonify({"status": "success", "reply": response_text}), 200
    
    else:
        return jsonify({"status": "ignored", "reason": "Message from self"}), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
