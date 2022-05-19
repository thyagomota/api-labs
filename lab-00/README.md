# Lab-00

## Quotes API (baseline)

Creation Date: April 24, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

The goal of this lab is to implement an API that returns a random quote. The quotes API has only one path, one entity, and no database requirements or parameters, favoring simplicity. 

The quotes used were based on [Kaggle's Quotes Dataset](https://www.kaggle.com/datasets/akmittal/quotes-dataset).

## Steps

### Step 1 - Virtual Environment

```
virtualenv venv
cd venv
source bin/activate
pip3 install -r ../requirements.txt
mkdir src
```

### Step 2 - API Specification

In a text editor, write [quotes.yaml](quotes.yaml) or copy the code:

```
cp ../quotes.yaml .
```

### Step 3 - Code Generator

Before running FastAPI code generator, update format.py because of a known bug in version 0.3.4. 

```
cp ../src/format.py lib/python3.8/site-packages/datamodel_code_generator
bin/fastapi-codegen --input quotes.yaml --output src
```

### Step 4 - Add the Controller

Add [controller.py](src/controller.py) to your code. 

```
cp ../src/controller.py src
```

### Step 5 - Modify the View


Modify main.py by replacing get_quote_0's implementation with the following. 

```
@app.get('/quotes/0', response_model=Quotes0GetResponse)
def get_quotes_0() -> Quotes0GetResponse:
    """
    Returns a random quote
    """
    return Quotes0GetResponse(
        status_code=200, 
        content_type='application/json',
        body=Controller.get_quotes_0()
    )
```

Don't forget to add the import statement.

```
from .controller import Controller
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quotes/0](http://127.0.0.1:8000/quotes/0).
