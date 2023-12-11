import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

# print(analyzer.polarity_scores('This is by far the worst movie I have ever seen!'))
# print(analyzer.polarity_scores('Absolutely amazing!'))
# print(analyzer.polarity_scores('This is a movie'))

# print(analyzer.polarity_scores('The economy has never been good'))
# print(analyzer.polarity_scores('The economy has never been so good'))

messages = []

def get_sentiment_score(c):
    return c.get('sentiment_score')

while True:
    new_message = input('Enter another message: ')
    scores = analyzer.polarity_scores(new_message)
    compound = scores.get('compound', 0)
    conversation = { 'message': new_message, 'sentiment_score': compound }
    messages.append(conversation)
    messages.sort(key=get_sentiment_score)
    print('Here are the messages, sorted by priority:')
    for message in messages:
        print(message)