# Lab-03

## Quotes API + SQL Database + Path & Query Parameters

Creation Date: April 28, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

This lab makes the quote’s id parameter optional by adding a new path without it, aimed to return a list of quotes that satisfy a set of criteria informed using the following (optional) query parameters:

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

Copy [quotes.yaml(../../lab-02/quotes.yaml) from [Lab 02](../lab-02). 

```
cp ../../lab-02/quotes.yaml .
```

Add the following path. 

```
  /quotes:
    get:
      summary: Returns a list of quotes that satisfy a search criteria
      parameters: 
        - in: query
          name: text
          schema: 
            type: string 
          required: false
          description: text that quote's text must contain
        - in: query
          name: author
          schema: 
            type: string
          required: false
          description: author of the quote to get
        - in: query
          name: category
          schema: 
            type: string
          required: false
          description: category of the quote to get  
        - in: query
          name: tag
          schema: 
            type: string
          required: false
          description: tag that quote must have
        - in: query
          name: popularity
          schema: 
            type: number
          required: false
          description: minimum popularity that quote must have     
      responses:
        200:
          description: A list of quotes
          content:
            application/json:
              schema: 
                type: array
                items: 
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

Modify main.py by replacing get_quotes_id from lab-02 and get_quotes with the following. 

```
@app.get('/quotes', response_model=List[dict], responses={'404': {'model': str}})
def get_quotes(
    text: Optional[str] = None,
    author: Optional[str] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    popularity: Optional[float] = None,
) -> Union[List[Quote], str]:
    """
    Returns a list of quotes that satisfy a search criteria
    """
    engine = DBHelper.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    if text: 
      result = result.filter(Quote.text.contains(text))
    if author:
      result = result.filter(Quote.author.contains(author))
    if category: 
      result = result.filter(Quote.category == category)
    if popularity: 
      result = result.filter(Quote.popularity >= float(popularity))
    if tag: 
      result = result.filter(Quote.tags.any(tag=tag))
    return [r.__dict__ for r in result]
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

Try opening the page [http://127.0.0.1:8000/quotes](http://127.0.0.1:8000/quotes). You should be able to retrieve a list with all the quotes in the database. Add filtering query parameters and see if the list returned is correct. 

You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```