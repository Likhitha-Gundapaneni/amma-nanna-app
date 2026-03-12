import requests
from bs4 import BeautifulSoup

def get_rythu_bandhu_status(farmer_id):
    try:
        url = "https://rythu-bandhu.telangana.gov.in/checkStatus"
        headers = {"User-Agent": "Mozilla/5.0"}
        payload = {"farmerId": farmer_id}
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        status_div = soup.find("div", {"class": "status-result"})
        if status_div and "credited" in status_div.text.lower():
            return {"status": "credited", "amount": "5000"}
        return {"status": "pending"}
    except Exception as e:
        print(f"Scraper error: {e}")
        return {"status": "error"}
