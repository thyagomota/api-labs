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
```

### Step 2 - Database Initialization

In a text editor, write [init_db.py](src/init_db.py) or copy the code. Then run it to create and populate the quotes database. 

```
cp ../src/init_db.py src
mkdir db
cp ../db/quotes.sql db
cp ../db/quotes.json db
python3 src/init_db.py
```

### Step 3 - API Specification

Copy and then run yamlgen.py to generate OAS schema data types from the data model. Yamlgen is an in-house Python script that creates schema data types in OAS-YAML format by extracting metadata from an SQLite database. Open-source DB introspection tools like yamlgen can be adapted to work with different databases as needed. 

```
cp ../src/yamlgen.py src
python3 src/yamlgen.py > quotes.yaml
```

Because yamlgen uses database introspection, the names of the schema data types names match the table names. Therefore, they are written in the plural form. Modify quotes.yaml by doing the following:

* change the schema data type names to their singular form.
* add the tags properties in Quote as an array of QuoteTag items.

```
        tags:
          type: array
          items: 
            $ref: "#/components/schemas/QuoteTag"
```

* add the /quotes/0 path.

```
paths:
  /quotes/0:
    get:
      summary: Returns a random quote
      responses:
        200:
          description: A random quote
          content:
            application/json:
              schema: 
                $ref: "#/components/schemas/Quote"
```

### Step 4 - Code Generator

Before running FastAPI code generator, update format.py because of a known bug in version 0.3.4. 

```
cp ../src/format.py lib/python3.8/site-packages/datamodel_code_generator
bin/fastapi-codegen --input quotes.yaml --output src
```

### Step 5 - Modify the Model

Run sqlacodegen to generate your API's model from the database. Sqlacodegen uses DB introspection to generate SQLAlchemy model code. SQLAlchemy is a popular choice for object-relational mapping in Python. 

```
bin/sqlacodegen sqlite:///db/quotes.db > src/models.py
```

Modify models.py by adding the following to the Quote class. 

```
    tags = relationship("QuoteTag", primaryjoin="Quote.id==QuoteTag.id", lazy="immediate") 
```

Comment the statement below found in QuoteTag. 

```
quote = relationship('Quote')
```

### Step 6 - Modify Main

Modify main.py by replacing get_quote_0's implementation with the following.

```
@app.get('/quotes/0', response_model=dict)
def get_quotes_0(response: Response) -> Quote:
    """
    Returns a random quote
    """
    engine = DBHelper.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    quote = result.order_by(func.random()).first()
    return quote.__dict__
```

FastAPI requires its response models to be pydantic-compatible. However, the Quote class in this lab is not a pydantic model anymore, but an SQLAlchemy model instead. One way around this problem is to change the value of the response_model annotation parameter in get_quotes_0 from Quotes to dict. 

The main.py code now requires a DBHelper class to connect to the database. 

Don't forget to add the import statements.

```
from fastapi import Response
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from .db_helper import DBHelper
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quotes/0](http://127.0.0.1:8000/quotes/0).

You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```