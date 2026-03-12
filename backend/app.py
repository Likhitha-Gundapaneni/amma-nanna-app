from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from voice.tts import speak_telugu
from nlp.intent_parser import detect_intent
from nlp.response_generator import generate_response
from scraper.rythu_bandhu import get_rythu_bandhu_status
from scraper.dharani import get_land_records

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {"message": "అమ్మ నాన్న App is Running! 🎤"}

@app.route("/process-voice", methods=["POST"])
def process_voice():
    try:
        telugu_text = request.form.get("text", "")
        print(f"Input: {telugu_text}")

        intent = detect_intent(telugu_text)
        print(f"Intent: {intent}")

        if intent == "rythu_bandhu_status":
            farmer_id = request.form.get("farmer_id", "")
            data = get_rythu_bandhu_status(farmer_id)
        elif intent == "land_records":
            survey_no = request.form.get("survey_no", "")
            district = request.form.get("district", "")
            data = get_land_records(survey_no, district)
        else:
            data = {"status": "unknown"}

        response_text = generate_response(intent, data)
        print(f"Response: {response_text}")

        speak_telugu(response_text, "response.mp3")
        return send_file("response.mp3", mimetype="audio/mpeg")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
