import random 
from .models import Quote

class Controller: 
    quotes = [
  {
    "Id": 1,   
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss",
    "Tags": [
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
    "Popularity": 0.15566615566615566,
    "Category": "life"
  },
  {
    "Id": 2,   
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss",
    "Tags": [
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
    "Popularity": 0.15566615566615566,
    "Category": "happiness"
  },
  {
    "Id": 3,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "love"
  },
  {
    "Id": 4,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "life"
  },
  {
    "Id": 5,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "truth"
  },
  {
    "Id": 6,   
    "Quote": "Be yourself; everyone else is already taken.",
    "Author": "Oscar Wilde",
    "Tags": [
      "attributed-no-source",
      "be-yourself",
      "honesty",
      "inspirational",
      "misattributed-oscar-wilde "
    ],
    "Popularity": 0.11322311322311322,
    "Category": "inspiration"
  },
  {
    "Id": 7,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "humor"
  },
  {
    "Id": 8,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "philosophy"
  },
  {
    "Id": 9,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "science"
  },
  {
    "Id": 10,   
    "Quote":
      "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
    "Author": "Bernard M. Baruch",
    "Tags": [
      "ataraxy",
      "be-yourself",
      "confidence",
      "fitting-in",
      "individuality",
      "those-who-matter "
    ],
    "Popularity": 0.10189010189010189,
    "Category": ""
  }]

    @staticmethod
    def get_quotes_0():
        raw_json = Controller.quotes[random.randint(0, len(Controller.quotes))]
        quote = Quote(
          id=raw_json['Id'], 
          text=raw_json['Quote'], 
          author=raw_json['Author'], 
          category=raw_json['Category'],
          popularity=raw_json['Popularity'],
          tags=raw_json['Tags'])
        return quote