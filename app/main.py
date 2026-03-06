from fastapi import FastAPI
from app.api.routes import router
from app.utils.logging import logger
from app.security.rate_limiter import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

app = FastAPI(
    title="Trade Opportunities API",
    version="1.0"
)

logger.info("Starting Trade Opportunities API")

# Rate limiter setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Trade Opportunities API Running"}