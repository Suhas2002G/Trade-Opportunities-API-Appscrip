from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse

from app.services.market_service import generate_sector_report
from app.security.auth import verify_api_key
from app.utils.logging import logger
from app.security.rate_limiter import limiter

router = APIRouter()


@router.get("/analyze/{sector}", response_class=PlainTextResponse)
@limiter.limit("2/minute")
async def analyze_sector_endpoint(
    request: Request,
    sector: str,
    auth: str = Depends(verify_api_key)
):

    try:
        logger.info(f"API request received for sector: {sector}")

        report = generate_sector_report(sector)
        return report

    except Exception as e:
        logger.error(f"API error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to generate sector analysis"
        )