# Lab-03

## Quotes API + SQL Database + Query Parameter

Creation Date: April 26, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 02](../lab-02). However, this implementation allows users to request that the returned random quote has a specific tag. 

The quotes used in this lab were based on [Kaggle's Quotes Dataset](https://www.kaggle.com/datasets/akmittal/quotes-dataset).

## Steps

Repeat all steps described in [Lab 02](../lab-02). 

### Step 1 - API Specification

Modify [quotes.yaml](quotes.yaml) by adding the following parameter: 

```
      parameters:
        - in: query
          name: tag
          description: A tag that the quote should list.
          schema: 
            type: string
```

### Step 2 - Code Generator

```
bin/fastapi-codegen --input quotes.yaml --output src
bin/sqlacodegen sqlite:///db/quotes.db > src/models.py
```

Modify [models.py](src/models.py) according to the TO-DOs embedded in the code. 

### Step 3 - Add controller.py

Add [controller.py](src/controller.py).

### Step 6 - Modify main.py

Replace get_quote's implementation with the following. 

```
@app.get('/quote')
def get_quote(tag=None) -> Quote:
    """
    Returns a random quote
    """
    quote = Controller.get_quote(tag=tag)
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
                'body': 'Quote not found!'
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
