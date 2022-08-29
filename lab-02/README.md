# Lab-02

## Quotes API + SQL Database + Path Parameter

Creation Date: April 28, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a single quote, with the same requirements of [Lab 01](../lab-01). In the previous lab, the <em>path</em> for a random quote was always set to zero. In this new lab the user can request a specific quote based on the quote's id indicated in the path. Because the requested quote might not exist, a 404 (Not Found) response was added to the API's specification. 

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

In a text editor, write [init_db.py](src/init_db.py) or copy the code. The run it to create and populate the quotes database. 

```
cp ../src/init_db.py src
mkdir db
cp ../db/quotes.sql db
cp ../db/quotes.json db
python3 src/init_db.py
```

### Step 3 - API Specification

Copy [quotes.yaml](../../lab-01/quotes.yaml) from [Lab 01](../lab-01). 

```
cp ../../lab-01/quotes.yaml .
```

Modify the paths section to the following. 

```
paths:
  /quotes/{id}:
    get:
      summary: Returns a quote given its id; for a random quote use id=0
      parameters: 
        - in: path
          name: id
          schema: 
            type: integer
          required: true
          description: id of the quote to get      
      responses:
        200:
          description: A quote
          content:
            application/json:
              schema: 
                $ref: "#/components/schemas/Quote"
        404: 
          description: Not Found
          content:
            "application/json":
              schema:
                type: string
```

### Step 4 - Code Generator

Before running FastAPI code generator, update format.py because of a known bug in version 0.3.4.

```
cp ../src/format.py lib/python3.8/site-packages/datamodel_code_generator
bin/fastapi-codegen --input quotes.yaml --output src
```

### Step 5 - Modify the Model

Run sqlacodegen to generate your API's model from the database. 

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
@app.get('/quotes/{id}', response_model=dict, responses={'404': {'model': str}})
def get_quotes_id(id: int) -> Union[dict, str]:
    """
    Returns a quote given its id; for a random quote use id=0
    """
    engine = DBHelper.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    quote = result.order_by(func.random()).first() if id == 0 else result.get(id)
    return quote.__dict__
```

Don't forget to copy db_helper.py. 

```
cp ../src/db_helper.py src
```

Also, don't forget to add the import statements.

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

Try opening the page [http://127.0.0.1:8000/quote](http://127.0.0.1:8000/quote).

You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```