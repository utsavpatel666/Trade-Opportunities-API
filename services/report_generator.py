def generate_report(sector: str, news: list, analysis: str):
    report = f"""
# Trade Opportunity Report – {sector.title()}

## 📰 Latest Market News
{news}

---

## 📈 AI Market Analysis
{analysis}

---

### Generated via FastAPI + Gemini API
"""
    return report
