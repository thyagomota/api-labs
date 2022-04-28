# Lab-02

## Quotes API + SQL Database + Path Parameter

Creation Date: April 28, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 01](../lab-01). In the previous lab, the <em>path</em> for a random quote was 0. In this new lab the user can request a specific quote based on the quote's id indicated in the path. Because the requested quote might not exist, a 404 (Not Found) response was added to the API's specification. 

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

Copy quotes.yaml from [Lab 01](../lab-01) and make the modifications described below: 

* change /quotes path's summary
* add an <em>id</em> path parameter to /quotes path. 
* add a 404 response to the same path. 

After the changes, quotes.yaml should look like [this](src/quotes.yaml)

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
  def get_quote(id):
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    if id == 0:
      quote = session.query(Quote).order_by(func.random()).first()
    else:
      quote = session.query(Quote).get(id)
    return quote
```

### Step 6 - Modify main.py

Replace get_quote's implementation with the following.  

```
@app.get('/quotes/0')
def get_quotes_0() -> Quote:
    """
    Returns a random quote
    """
    quote = Controller.get_quote()
    return {
        'statusCode': 200, 
        'Content-Type': 'application/json',
        'body': {
            'quote': quote.toJSON(), 
        }
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

Try opening the page [http://127.0.0.1:8000/quote](http://127.0.0.1:8000/quote).
