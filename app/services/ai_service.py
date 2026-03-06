

from google import genai
from app.config.settings import settings
from app.utils.logging import logger

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def analyze_sector(sector, news):

    logger.info(f"Sending sector data to Gemini for analysis: {sector}")

    news_text = "\n".join(
        [f"{n['title']} - {n['body']}" for n in news]
    )

    prompt = f"""
        Analyze the Indian {sector} sector.

        News:
        {news_text}

        Provide:
        1 Market Overview
        2 Opportunities
        3 Risks
        4 Conclusion
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        logger.info("Gemini analysis successful")

        return response.text

    except Exception as e:

        logger.error(f"Gemini API failed: {str(e)}")

        raise Exception("AI analysis failed")