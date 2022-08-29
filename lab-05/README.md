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

In a text editor, write [init_db.py](src/init_db.py) or copy the code. The run it to create and populate the quotes database. Note that a new table named "keys" was added with a few rows to allow authentication testing. 

```
cp ../src/init_db.py src
mkdir db
cp ../db/quotes.sql db
cp ../db/quotes.json db
python3 src/init_db.py
```

### Step 3 - API Specification

Copy [quotes.yaml(../../lab-04/quotes.yaml) from [Lab 04](../lab-04). 

```
cp ../../lab-04/quotes.yaml .
```

Add the following key parameter to both paths. 

```
        - in: query
          name: key
          schema: 
            type: string
          required: true 
```

Add the following response to both paths. 

```
        401: 
          description: Unauthorized
          content:
            application/json:
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

### Step 7 - Modify main.py

Copy main.py from [Lab-04](../lab-04). 

```
cp ../../lab-04/src/main.py src
```

Modify both "get_quotes_id" and "get_quotes" so those functions check whether a valid "key" was informed (i.e., a user can be authenticated).

Don't forget to copy db_helper.py.

```
cp ../src/db_helper.py src
```

You will also need to import the Key model. 

```
from .models import Key
```

You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Test the API using valid keys. Make sure all of the previous parameters still work.


You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```