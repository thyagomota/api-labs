# Lab-03

## Quotes API + SQL Database + Path Parameter + Query Parameters

Creation Date: April 28, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

This lab is built on top of [Lab 02](../lab-02) with the addition of (optional) query parameters:

* text that quote's text must contain
* author of the quote to get
* category of the quote to get
* tag that quote must have
* minimum popularity that quote must have

## Steps

### Step 1 - Virtual Environment

```
virtualenv venv
cd venv
source bin/activate
pip3 install -r ../requirements.txt
mkdir src
```

### Step 2 - Database

Run [init_db.py](src/init_db.py) to create and populate the quotes database. 

### Step 3 - API Specification

Copy quotes.yaml from [Lab 02](../lab-02) and add query parameters to /quotes path. After the changes, quotes.yaml should look like [this](src/quotes.yaml)

### Step 4 - Code Generator

```
bin/fastapi-codegen --input ../quotes.yaml --output src
bin/sqlacodegen sqlite:///db/quotes.db > src/models.py
```

Modify [models.py](src/models.py) according to the notes embedded in the code. 

### Step 5 - Add controller.py

Replace get_quote's implementation from [Lab 01](../lab-01) with the following: 

```
  # NOTE: following method has been modified
  @staticmethod
  def get_quote(id, text=None, author=None, category=None, tag=None, popularity=None):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if id == 0: 
      result = session.query(Quote)
      if text: 
        result = result.filter(Quote.text.contains(text))
      if author:
        result = result.filter(Quote.author.contains(author))
      if category: 
        result = result.filter(Quote.category == category)
      if popularity: 
        result = result.filter(Quote.popularity >= popularity)
      if tag: 
        result = result.filter(Quote.tags.any(tag=tag))
      quote = result.order_by(func.random()).first()
    else:
      quote = session.query(Quote).get(id)
    return quote
```

### Step 6 - Modify main.py

Replace get_quote's implementation with the following.  

```
# NOTE: following method has been modified
@app.get('/quotes/{id}')
def get_quotes_id(id: int, text=None, author=None, category=None, tag=None, popularity=None) -> Quote:
    quote = Controller.get_quote(id, text=text, author=author, category=category, tag=tag, popularity=popularity)
    if quote:
        return {
            'statusCode': 200, 
            'Content-Type': 'application/json',
            'body': {
                'quote': quote.toJSON(), 
            }
        } 
    else:
        return {
            'statusCode': 404, 
            'Content-Type': 'application/json',
            'body': 'Not Found'
        }  
```

Also, add the following import statement: 

```
from .controller import Controller
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quotes/0](http://127.0.0.1:8000/quotes/0).
