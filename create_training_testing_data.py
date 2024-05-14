import csv
import random
from get_score_NLP import SentenceQuality

def split_data(reader, train_writer, test_writer, test_ratio=0.2):
    for row in reader:
        scores = obj.calculateScores(row['text'], row['time_created'], float(row['weather']))
        quality_score = obj.calculateQuality(scores)
        row['score'] = quality_score
        
        if random.random() < test_ratio:
            test_writer.writerow(row)
        else:
            train_writer.writerow(row)

obj = SentenceQuality()
with open('reviews.csv', mode='r', newline='', encoding='utf-8') as file, \
        open('training_data.csv', mode='w', newline='', encoding='utf-8') as train_file, \
        open('testing_data.csv', mode='w', newline='', encoding='utf-8') as test_file:
    
    reader = csv.DictReader(file)
    train_writer = csv.DictWriter(train_file, fieldnames=reader.fieldnames + ['score'])
    test_writer = csv.DictWriter(test_file, fieldnames=reader.fieldnames + ['score'])
    
    train_writer.writeheader()
    test_writer.writeheader()
    
    split_data(reader, train_writer, test_writer)
