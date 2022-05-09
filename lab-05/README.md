# Lab-05

## Quotes API + SQL Database + Path Parameter + Query Parameters + Pagination + Authentication

Creation Date: May 09, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

A key parameter is added to Quotes API to provide a simple authentication mechanism. 

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

Run [init_db.py](src/init_db.py) to create and populate the quotes database. Note that a new table named "keys" was added with a few rows to allow authentication testing. 

### Step 3 - API Specification

Copy quotes.yaml from [Lab 04](../lab-04) and add a new key parameter and response to both paths. After the changes, quotes.yaml should look like [this](src/quotes.yaml)

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

Add the following method and import statement: 

```
# NOTE: following import has been added
from .models import Key

  # NOTE: following method has been added
  @staticmethod
  def is_authenticated(key): 
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Key).get(key)
    return True if result else False
```

### Step 6 - Modify main.py

Modify get_quote's function.   

```
# NOTE: following method has been modified
@app.get('/quotes')
def get_quotes(text=None, author=None, category=None, tag=None, popularity=None, offset=0, limit=10, key=None):
    if Controller.is_authenticated(key):
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
    else: 
        return {
            'statusCode': 401, 
            'Content-Type': 'application/json',
            'body': 'Unauthorized'
        }  
```

Modify get_quote_id's function.  

```
# NOTE: following method has been modified
@app.get('/quotes/{id}')
def get_quotes_id(id: int, text=None, author=None, category=None, tag=None, popularity=None, key=None):
    if Controller.is_authenticated(key):
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
    else: 
        return {
            'statusCode': 401, 
            'Content-Type': 'application/json',
            'body': 'Unauthorized'
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

Test the API using valid keys. Make sure all of the previous parameters still work. 