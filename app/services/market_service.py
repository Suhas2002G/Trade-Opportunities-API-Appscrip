from app.services.search_service import search_market_news
from app.services.ai_service import analyze_sector
from app.utils.markdown import generate_markdown
from app.utils.logging import logger


def generate_sector_report(sector):

    try:

        logger.info(f"Generating report for sector: {sector}")

        news = search_market_news(sector)

        analysis = analyze_sector(sector, news)

        report = generate_markdown(sector, analysis)

        logger.info("Report generated successfully")

        return report

    except Exception as e:

        logger.error(f"Report generation failed: {str(e)}")

        raise Exception("Sector analysis failed")