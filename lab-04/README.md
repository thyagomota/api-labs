# Lab-04

## Quotes API + SQL Database + Path Parameter + Query Parameters + Pagination

Creation Date: May 06, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

API pagination gives users the ability to select which group of objects of the same type to return. This lab implements a limit-offset pagination of quotes that fit a given search criteria. Two more (optional) parameters were added to the ones described in [Lab 03](../lab-03): 

* offset: how many quotes should be skipped
* limit: the maximum number of quotes to be returned

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

In a text editor, write [init_db.py](src/init_db.py) or copy the code. The run it to create and populate the quotes database. 

```
cp ../src/init_db.py src
mkdir db
cp ../db/quotes.sql db
cp ../db/quotes.json db
python3 src/init_db.py
```

### Step 3 - API Specification

Copy [quotes.yaml(../../lab-03/quotes.yaml) from [Lab 03](../lab-03). 

```
cp ../../lab-03/quotes.yaml .
```

Add the following query parameters to "/quotes" path. 

```
        - in: query
          name: offset
          schema:
            type: number 
          required: false 
          description: how many quotes should be skipped (defaults to zero)
        - in: query 
          name: limit 
          schema: 
            type: number 
          required: false
          description: the maximum number of quotes to be returned (defaults to 10)
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

Copy [controller.py(../../lab-03/src/controller.py) from [Lab 03](../lab-03). 

```
cp ../../lab-03/src/controller.py src
```

Add parameters offset (with a default value of 0) and limit (with a default value of 10) to the "get_quotes" method. Then add the following statement right after the method's return. 

```
    result = result.offset(offset).limit(limit)
```

### Step 7 - Modify main.py

Copy main.py from [Lab-03](../lab-03). 

```
cp ../../lab-03/src/main.py src
```

Add parameters offset (with a default value of 0) and limit (with a default value of 10) to the "get_quotes" function. Make sure to pass those parameters to the controller's "get_quotes" method. 

## Test & Validation

```
bin/uvicorn src.main:app
```

Test if pagination works. Make sure all of the previous parameters still work. 

You can also write a [client.py](src/client.py) script or copy the code.

```
cp ../src/client.py src
```

## Challenge

Change the API's pagination parameters to use (page, page_size) instead of (offset, limit) by having: 

* offset = (page - 1) * page_size
* limit = page_size
