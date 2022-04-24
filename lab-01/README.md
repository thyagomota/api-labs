# Lab-01

## Quotes API

Creation Date: April 24, 2022

Original Author(s): [Thyago Mota](https://github.com/thyagomota)

Contributor(s): 

## Goals

* Implement a simple API with only one path, one entity, and no database requirements or parameters. 


### Step 1 - Virtual Environment

```
virtualenv venv
cd venv
source bin/activate
pip3 install -r requirements.txt
mkdir src
```

### Step 2 - API Specification

In a text editor, write [quotes.yaml](quotes.yaml) as follows. 

### Step 3 - Code Generator

```
bin/fastapi-codegen --input quotes.yaml --output src
```

### Step 4 - Add controller.py

Add [controller.py](src/controller.py).

### Step 5 - Modify main.py

Replace get_quote's implementation with: 

```
@app.get('/quote', response_model=None)
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
