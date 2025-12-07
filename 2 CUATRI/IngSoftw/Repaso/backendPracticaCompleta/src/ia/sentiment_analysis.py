pipeline = None

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


class SentimentModel:
    @staticmethod
    def analyze_sentiment(text):
        if pipeline:
            prediction = pipeline(text)
            label = prediction[0][0]['label']
            return label
        else:
            import random
            labels = ["positive", "negative", "neutral"]
            label = random.choice(labels)
            return label

if __name__ == "__main__":
    if torch.cuda.is_available():
        print("CUDA is available. Using GPU.")
    else:
        print("CUDA is not available. Using CPU.")
    print(SentimentModel.analyze_sentiment("I love this movie!")) # positive
    print(SentimentModel.analyze_sentiment("I hate this movie!")) # negative
    print(SentimentModel.analyze_sentiment("I don't know how I feel about this movie...")) # neutral
