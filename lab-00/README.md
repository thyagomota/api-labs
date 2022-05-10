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

In a text editor, write [quotes.yaml](quotes.yaml). 

### Step 3 - Code Generator

Before running FastAPI code generator, you need to update format.py because of a known bug in version 0.3.4. 

```
cp src/format.py lib/python3.8/site-packages/datamodel_code_generator
bin/fastapi-codegen --input ../quotes.yaml --output src
```

### Step 4 - Update Code

Modify models.py  by adding the following method to the Quote class. 

```
    def toJSON(self):
        return {
            'id': self.id, 
            'text': self.text, 
            'author': self.author, 
            'popularity': self.popularity, 
            'category': self.category, 
            'tags': self.tags
        }
```

Copy [controller.py](src/controller.py).

```
cp ../src/controller.py src
```

Modify main.py by replacing get_quote_0's implementation with the following. 

```
@app.get('/quotes/0', response_model=Quotes0GetResponse)
def get_quotes_0() -> Quotes0GetResponse:
    """
    Returns a random quote
    """
    quote = Controller.get_quote()
    return {
        'statusCode': 200, 
        'Content-type': 'application/json', 
        'body': quote.toJSON()
    }
```

Also in main.py, add the following import statement.

```
from .controller import Controller
```

## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quotes/0](http://127.0.0.1:8000/quotes/0).
