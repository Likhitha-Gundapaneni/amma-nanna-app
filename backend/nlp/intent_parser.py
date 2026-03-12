INTENTS = {
    "rythu_bandhu_status": [
        "రైతు బంధు", "డబ్బులు పట్టాయా", "సహాయం వచ్చిందా",
        "అకౌంట్లో వేశారా", "పైసలు వచ్చాయా"
    ],
    "land_records": [
        "పట్టా", "భూమి రికార్డు", "ధరణి",
        "సర్వే నంబర్", "ల్యాండ్ రికార్డ్"
    ],
    "ration_card": [
        "రేషన్ కార్డు", "బియ్యం వచ్చాయా", "రేషన్ షాప్"
    ],
    "pension_status": [
        "పెన్షన్", "వృద్ధాప్య పెన్షన్", "పెన్షన్ వచ్చిందా"
    ]
}

def detect_intent(telugu_text):
    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in telugu_text:
                return intent
    return "unknown"
