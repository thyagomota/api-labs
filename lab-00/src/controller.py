import random 

from .models import Quote

class Controller: 

    quotes = [
  {
    "id": 1,   
    "text": "Don't cry because it's over, smile because it happened.",
    "author": "Dr. Seuss",
    "tags": [
      "attributed-no-source",
      "cry",
      "crying",
      "experience",
      "happiness",
      "joy",
      "life",
      "misattributed-dr-seuss",
      "optimism",
      "sadness",
      "smile",
      "smiling "
    ],
    "popularity": 0.15566615566615566,
    "category": "life"
  },
  {
    "id": 2,   
    "text": "Don't cry because it's over, smile because it happened.",
    "author": "Dr. Seuss",
    "tags": [
      "attributed-no-source",
      "cry",
      "crying",
      "experience",
      "happiness",
      "joy",
      "life",
      "misattributed-dr-seuss",
      "optimism",
      "sadness",
      "smile",
      "smiling "
    ],
    "popularity": 0.15566615566615566,
    "category": "happiness"
  },
  {
    "id": 3,   
    "text":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "author": "Marilyn Monroe",
    "tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "popularity": 0.12912212912212911,
    "category": "love"
  },
  {
    "id": 4,   
    "text":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "author": "Marilyn Monroe",
    "tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "popularity": 0.12912212912212911,
    "category": "life"
  },
  {
    "id": 5,   
    "text":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "author": "Marilyn Monroe",
    "tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "popularity": 0.12912212912212911,
    "category": "truth"
  },
  {
    "id": 6,   
    "text": "Be yourself; everyone else is already taken.",
    "author": "Oscar Wilde",
    "tags": [
      "attributed-no-source",
      "be-yourself",
      "honesty",
      "inspirational",
      "misattributed-oscar-wilde "
    ],
    "popularity": 0.11322311322311322,
    "category": "inspiration"
  },
  {
    "id": 7,   
    "text":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "author": "Albert Einstein",
    "tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "popularity": 0.10312710312710313,
    "category": "humor"
  },
  {
    "id": 8,   
    "text":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "author": "Albert Einstein",
    "tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "popularity": 0.10312710312710313,
    "category": "philosophy"
  },
  {
    "id": 9,   
    "text":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "author": "Albert Einstein",
    "tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "popularity": 0.10312710312710313,
    "category": "science"
  },
  {
    "id": 10,   
    "text":
      "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
    "author": "Bernard M. Baruch",
    "tags": [
      "ataraxy",
      "be-yourself",
      "confidence",
      "fitting-in",
      "individuality",
      "those-who-matter "
    ],
    "popularity": 0.10189010189010189,
    "category": ""
  }]

    @staticmethod
    def get_quote():
        raw_json = Controller.quotes[random.randint(0, len(Controller.quotes))]
        quote = Quote(id=raw_json['id'], text=raw_json['text'], author=raw_json['author'])
        quote.category = raw_json['category']
        quote.popularity = raw_json['popularity']
        quote.tags = raw_json['tags']
        return quote