# Lab-04

## Quotes API + SQL Database + Path Parameter + Query Parameters + Pagination

Creation Date: May 06, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

API pagination gives users the ability to select which group of objects of the same type to return. This lab implements a limit-offset pagination of quotes that fit a given search criteria. Two more (optional) parameters were added to the ones described in [Lab 03](../lab-03): 

* offset: how many quotes should be skipped
* limit: the maximum number of quotes to be returned

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

Copy quotes.yaml from [Lab 03](../lab-03) and add a new /quotes path (with the {id} parameter). After the changes, quotes.yaml should look like [this](src/quotes.yaml)

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
  def get_quote(id=None, text=None, author=None, category=None, tag=None, popularity=None, offset=0, limit=10):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if not id or id == 0: 
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
      if not id:        
        return result.order_by(Quote.id).offset(offset).limit(limit)
      else:
        return result.order_by(func.random()).first()
    else:
      return session.query(Quote).get(id)
```

### Step 6 - Modify main.py

Modify get_quote's function.   

```
# NOTE: following method has been added
@app.get('/quotes')
def get_quotes(text=None, author=None, category=None, tag=None, popularity=None, offset=0, limit=10):
    result = Controller.get_quote(text=text, author=author, category=category, tag=tag, popularity=popularity, offset=offset, limit=limit)
    if result:
        quotes = []
        for quote in result: 
            quotes.append(quote.toJSON())
        if len(quotes) > 0:
            return {
                'statusCode': 200, 
                'Content-Type': 'application/json',
                'body': {
                    'quotes': quotes, 
                }
            }
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

Test if pagination works. Make sure all of the previous parameters still work. 

## Challenge

Change the API's pagination parameters to use (page, page_size) instead of (offset, limit) by having: 

* offset = (page - 1) * page_size
* limit = page_size
