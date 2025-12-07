from fastapi import APIRouter
from .pydantic_models import SentimentRequest
from ia import SentimentModel  

router = APIRouter()

@router.post("/analyze")
async def analyze(request: SentimentRequest):
    text = request.text
    sentiment = SentimentModel.analyze_sentiment(text)  # Llamada asíncrona al servicio de inferencia

    return {"sentiment": sentiment}
