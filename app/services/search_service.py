from ddgs import DDGS
from app.utils.logging import logger


def search_market_news(sector: str):

    logger.info(f"Searching market news for sector: {sector}")

    query = f"India {sector} sector news market growth"

    results = []

    try:

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):

                results.append({
                    "title": r["title"],
                    "body": r["body"],
                    "link": r["href"]
                })

        logger.info(f"Collected {len(results)} news articles")

        return results

    except Exception as e:

        logger.error(f"Search service failed: {str(e)}")

        raise Exception("Failed to collect market news")