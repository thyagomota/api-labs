# Lab-01

## Quotes API + SQL Database

Creation Date: April 26, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 00](../lab-00). However, this time the quotes are stored in an (embedded) SQL database (sqlite). Also, object-relational mapping was implemented using SQLAlchemy. 

## Steps

### Step 1 - Virtual Environment

```
virtualenv venv
cd venv
source bin/activate
pip3 install -r ../requirements.txt
mkdir src
mkdir db
```

### Step 2 - Database


Copy and then run init_db.py to create and populate the quotes database. 

```
cp ../src/init_db.py src
python3 src/init_db.py
```

### Step 3 - API Specification

Copy and then run yamlgen.py to generate <em>schema data types</em> from the data model. 

```
cp ../src/yamlgen.py src
python3 src/yamlgen.py
```

Because yamlgen uses database introspection, the names of the <em>schema data types</em> names match the table names. Therefore, they are written in the plural form. Modify quotes.yaml by doing the following: 

* change the <em>schema data type</em> names to their singular form. 
* add the <em>tags</em> properties in <em>quotes</em> as an array of <em>QuoteTag</em> items. 
* add the /quote path. 

### Step 4 - Code Generator

Before running FastAPI code generator, you need to update format.py because of a known bug in version 0.3.4.

```
cp ../src/format.py lib/python3.8/site-packages/datamodel_code_generator
bin/fastapi-codegen --input ../quotes.yaml --output src
```

Run sqlacodegen to generate your API's model from the specification. 

```
bin/sqlacodegen sqlite:///db/quotes.db > src/models.py
```

### Step 5 - Update Code

Modify models.py by adding the following to the Quote class. 

```
    tags = relationship("QuoteTag", primaryjoin="Quote.id==QuoteTag.id") 

    def toJSON(self):
        ret = {}
        ret['id'] = self.id
        ret['text'] = self.text
        ret['author'] = self.author 
        ret['popularity'] = self.popularity 
        ret['category'] = self.category
        ret['tags'] = []
        for tag in self.tags:
            ret['tags'].append(tag.tag)
        return ret
```

Comment the statement below found in QuoteTag. 

```
quote = relationship('Quote')
```

Copy controller.py.

```
cp ../src/controller.py src
```

Modify main.py by replace get_quote's implementation with the following.  

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

Also in main.py, add the following import statement. 

```
from .controller import Controller
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quote](http://127.0.0.1:8000/quote).
