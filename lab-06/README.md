# Lab-06

## Quotes API + SQL Database

Creation Date: May 09, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote, similarly to [Lab 00](lab-00). However, this time the quotes are stored in a NoSQL database (MongoDB). Also, object-relational mapping was implemented using mongoengine.

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

Run [init_db.py](src/init_db.py) to create and populate the quotes database. Make sure to update the db connection parameters in config.properties. 

### Step 3 - API Specification

Run [yamlgen](src/yamlgen.py) to generate <em>schema data types</em> from the data model. Note that because [yamlgen](src/yamlgen.py) uses database introspection, the names of the <em>schema data types</em> names match the table names. Therefore, they are kept in the plural form.  

Modify [quotes.yaml](quotes.yaml) by doing the following: 

* change the <em>schema data type</em> names to their singular form. 
* add the <em>tags</em> properties in <em>quotes</em> as an array of <em>QuoteTag</em> items. 
* add the /quote path. 

### Step 4 - Code Generator

```
bin/fastapi-codegen --input ../quotes.yaml --output src
```

Remove models.py since we will use the documents returned from MongoDB as python dictionary objects directly. 

### Step 5 - Add controller.py

Add [controller.py](src/controller.py).

### Step 6 - Modify main.py

Replace get_quote's implementation with the following.  

```
# NOTE: following method has been modified
@app.get('/quotes/0')
def get_quotes_0():
    """
    Returns a random quote
    """
    quote = Controller.get_quote()
    return {
        'statusCode': 200, 
        'Content-Type': 'application/json',
        'body': {
            'quote': quote, 
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
