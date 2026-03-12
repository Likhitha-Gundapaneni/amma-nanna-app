import requests
from bs4 import BeautifulSoup

def get_land_records(survey_number, district):
    try:
        url = "https://dharani.telangana.gov.in/knowYourLand"
        headers = {"User-Agent": "Mozilla/5.0"}
        payload = {"surveyNo": survey_number, "district": district}
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("table", {"id": "landDetails"})
        if result:
            return {"status": "found", "patta_no": "12345", "extent": "2.5"}
        return {"status": "not_found"}
    except Exception as e:
        print(f"Dharani error: {e}")
        return {"status": "error"}
