from fastapi import FastAPI
from transformers import pipeline
import random

from api import SentimentRequest

sentiment_pipeline = None
try:
    import os
    # Comenta esta línea si quieres usar la GPU
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    import torch
    from transformers import pipeline
    pipeline = pipeline(
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
        top_k=None
    )
except:
    pass
    

app = FastAPI()

@app.post("/analyze")
async def analyze(request: SentimentRequest):
    text = request.text.lower()
    
    if sentiment_pipeline:
        prediction = sentiment_pipeline(text)
        best_label = max(prediction[0], key=lambda x: x['score'])['label'].lower()
    else:
        best_label = random.choice(["positive", "negative", "neutral"])

    return {"sentiment": best_label}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("inference_service:app", host="0.0.0.0", port=8001, reload=True)
