from fastapi import APIRouter, Request, Depends, HTTPException
from utils.auth import verify_token
from utils.rate_limiter import limiter
from utils.validator import validate_sector_name
from services.data_collect import get_sector_news
from services.ai_engine import analyze_data
from services.report_generator import generate_report

router = APIRouter(prefix="/analyze", tags=["Analysis"])

@router.get("/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    sector: str,
    request: Request,
    token: str = Depends(verify_token)
):
    validate_sector_name(sector)

    news = get_sector_news(sector)

    ai_analysis = analyze_data(sector, news)

    report = generate_report(sector, news, ai_analysis)

    return {"sector": sector, "report": report}
