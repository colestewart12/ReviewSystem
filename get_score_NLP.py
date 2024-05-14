from textblob import TextBlob
import datetime

class SentenceQuality:
    def __init__(self):
        pass

    def calculateScores(self, text, time_created, weather):
        blob = TextBlob(text)
        characters = len(text)
        words = len(blob.words)
        sentences = len(blob.sentences)
        
        readability = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        coleman_liau_index = (0.0588 * (characters / words) * 100) - (0.296 * (sentences / words) * 100) - 15.8
        subjectivity = blob.sentiment.subjectivity
        polarity = blob.sentiment.polarity
        
        time = datetime.datetime.strptime(time_created, "%Y-%m-%d %H:%M:%S")
        hour = time.hour
        is_weekend = 1 if time.weekday() > 4 else 0
        
        normalized_temp = (weather - 30) / 50  # Assuming typical range from 30F to 80F

        return [readability, subjectivity, polarity, words, coleman_liau_index, hour, is_weekend, normalized_temp]

    def calculateQuality(self, scores):
        weights = {
            'readability': 0.15,
            'subjectivity': 0.15,
            'polarity': 0.15,
            'words': 0.1,
            'coleman_liau': 0.15,
            'hour': 0.1,
            'weekend': 0.1,
            'temperature': 0.1
        }
        
        max_scores = [10, 1.0, 1.0, 100, 20, 24, 1, 1]
        normalized_scores = [min(max(score / max_val, 0), 1) for score, max_val in zip(scores, max_scores)]
        
        overall_score = sum(weight * score for weight, score in zip(weights.values(), normalized_scores))
        
        return overall_score

obj = SentenceQuality()
review = "Just went here, great food and good portion. Love the kim chi box. The service and place was clean."
time_created = "2024-03-28 12:33:17"
weather = 58.658

scores = obj.calculateScores(review, time_created, weather)
quality_score = obj.calculateQuality(scores)
print("Calculated quality score:", quality_score)
