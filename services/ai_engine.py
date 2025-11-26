import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def analyze_data(sector: str, news: list):
    if not API_KEY:
        return "AI key not found. Using fallback basic analysis."

    prompt = f"""
    You are an economic analyst. Analyze the latest Indian market updates
    for the {sector} sector.

    News Data:
    {news}

    Provide:
    - Market summary
    - Growth factors
    - Risk factors
    - Investment opportunities
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
