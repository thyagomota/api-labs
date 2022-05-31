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

### Step 6 - Add the Controller

In a text editor, write [controller.py](src/controller.py) or copy the code. 

```
cp ../src/controller.py src
```

### Step 7 - Modify main.py

Copy main.py from [Lab-02](../lab-02). 

```
cp ../../lab-02/src/main.py src
```

Add the "get_quotes" function described below.  

```
@app.get('/quotes')
def get_quotes(
    response: Response,
    text: Optional[str] = None,
    author: Optional[str] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    popularity: Optional[float] = None) -> List[Quote]:
    """
    Returns a list of quotes that satisfy a search criteria
    """
    quotes = Controller.get_quotes(text, author, category, tag, popularity)
    if quotes:
        response.status_code = 200
        return quotes
    else:
        response.status_code = 404
        return {'message': 'Not found!'}
```

"Optional" needs to be imported from typing.

```
from typing import Optional
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