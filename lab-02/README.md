# Lab-02

## Quotes API + SQL Database

Creation Date: April 26, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 01](../lab-01). However, this time the quotes are stored in an embedded SQL database (sqlite). Also, object-relational mapping was implemented using SQLAlchemy. 

The quotes used in this lab were based on [Kaggle's Quotes Dataset](https://www.kaggle.com/datasets/akmittal/quotes-dataset).

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

Run [yamlgen](src/yamlgen.py) to generate the schema data types from the data model. Note that because yamlgen uses database introspection, the names of the schema data types match the table names. Therefore, they are kept in the plural form. 

Modify [quotes.yaml](quotes.yaml) by doing the following: 

* change the schema data type names to the singular form. 
* add the tags properties in quotes, as an array of QuoteTag items. 
* add the /quote path. 

### Step 4 - Code Generator

```
bin/fastapi-codegen --input quotes.yaml --output src
bin/sqlacodegen sqlite:///db/quotes.db > src/models.py
```

Modify [models.py](src/models.py) according to the TO-DOs embedded in the code. 

### Step 5 - Add controller.py

Add [controller.py](src/controller.py).

### Step 6 - Modify main.py

Replace get_quote's implementation with: 

```
@app.get('/quote')
def get_quote() -> None:
    """
    Returns a random quote
    """
    return Controller.get_quote()
```

Add the following import statement: 

```
from .controller import Controller
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quote](http://127.0.0.1:8000/quote).
