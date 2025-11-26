def generate_report(sector: str, news: list, analysis: str):
    report = f"""
# Trade Opportunity Report – {sector.title()}

{news}

---

{analysis}

---

"""
    return report
