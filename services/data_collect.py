import requests

def get_sector_news(sector: str):
    url = f"https://duckduckgo.com/?q={sector}+india+market&format=json"
    try:
        res = requests.get(url)
        return res.json().get("RelatedTopics", [])
    except:
        return ["Unable to fetch news due to API issue."]
