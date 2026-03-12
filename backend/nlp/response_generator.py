RESPONSES = {
    "rythu_bandhu_credited":
        "నాన్న, మీ రైతు బంధు డబ్బులు అకౌంట్లో క్రెడిట్ అయ్యాయి. ఈ సీజన్ {amount} రూపాయలు వచ్చాయి.",
    "rythu_bandhu_pending":
        "నాన్న, ఈ సారి ఇంకా డబ్బులు రాలేదు. కొంచెం వేచి చూడండి.",
    "land_records_found":
        "నాన్న, మీ పట్టా నంబర్ {patta_no}. విస్తీర్ణం {extent} ఎకరాలు.",
    "land_records_not_found":
        "నాన్న, ఆ సర్వే నంబర్ కి రికార్డులు దొరకలేదు. మళ్ళీ ట్రై చేయండి.",
    "error":
        "నాన్న, ఇప్పుడు సర్వర్ బిజీగా ఉంది. కొంచెం తర్వాత మళ్ళీ అడగండి.",
    "unknown":
        "నాన్న, మీరు అడిగింది నాకు అర్థం కాలేదు. మళ్ళీ చెప్పండి."
}

def generate_response(intent, data={}):
    key = f"{intent}_{data.get('status', 'error')}"
    template = RESPONSES.get(key, RESPONSES["unknown"])
    try:
        return template.format(**data)
    except:
        return RESPONSES["error"]
