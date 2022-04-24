import random 

class Controller: 

    quotes = [
  {
    "text": "Myths which are believed in tend to become true.",
    "author": "George Orwell",
    "tags": ["famous-quotes"]
  },
  {
    "text": "In all chaos there is a cosmos, in all disorder a secret order.",
    "author": "Carl Jung",
    "tags": ["famous-quotes"],
  },
  {
    "text": "Be courteous to all, but intimate with few, and let those few be well tried before you give them your confidence.",
    "author": "George Washington",
    "tags": ["friendship"]
  },
  {
    "text": "If you break your neck, if you have nothing to eat, if your house is on fire, then you got a problem. Everything else is inconvenience.",
    "author": "Robert Fulghum",
    "tags": ["famous-quotes"]
  },
  {
    "text": "The past has no power to stop you from being present now. Only your grievance about the past can do that.",
    "author": "Eckhart Tolle",
    "tags": ["famous-quotes"]
  },
  {
    "text": "There is nothing happens to any person but what was in his power to go through with.",
    "author": "Marcus Aurelius",
    "tags": ["famous-quotes"]
  },
  {
    "text": "The smallest act of kindness is worth more than the grandest intention.",
    "author": "Oscar Wilde",
    "tags": ["famous-quotes"]
  },
  {
    "text": "Not what we have but what we enjoy constitutes our abundance.",
    "author": "Jean Antoine Petit-Senn",
    "tags": ["famous-quotes"]
  },
  {
    "text": "Never tell people how to do things. Tell them what to do and they will surprise you with their ingenuity.",
    "author": "George S. Patton",
    "tags": ["wisdom"]
  },
  {
    "text": "A really great talent finds its happiness in execution.",
    "author": "Johann Wolfgang von Goethe",
    "tags": ["famous-quotes", "happiness"]
  }]

    @staticmethod
    def get_quote():
        return Controller.quotes[random.randint(0, len(Controller.quotes))]