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

Copy and then run [init_db.py](src/init_db.py) to create and populate the quotes database.

```
cp ../src/init_db.py src
mkdir db
cp ../db/quotes.sql db
cp ../db/quotes.json db
python3 src/init_db.py
```

### Step 3 - API Specification

Copy quotes.yaml from [Lab 01](../lab-01). 

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
            "application/json":
              schema:
                required:
                  - status_code
                  - content_type
                  - body
                properties:
                  status_code: 
                    type: integer
                  content_type: 
                    type: string 
                  body: 
                    $ref: "#/components/schemas/Quote"
        404: 
          description: Not Found
          content:
            "application/json":
              schema:
                required:
                  - status_code
                  - content_type
                  - body
                properties:
                  statusCode: 
                    type: integer
                  Content-type: 
                    type: string 
                  body: 
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
    tags = relationship("QuoteTag", primaryjoin="Quote.id==QuoteTag.id") 

    def toJSON(self):
        ret = {}
        ret['id'] = self.id
        ret['text'] = self.text
        ret['author'] = self.author 
        ret['popularity'] = self.popularity 
        ret['category'] = self.category
        ret['tags'] = []
        for tag in self.tags:
            ret['tags'].append(tag.tag)
        return ret
```

Comment the statement below found in QuoteTag.

```
quote = relationship('Quote')
```

Finally, add the QuotesIdGetResponse class.

```
class QuotesIdGetResponse(BaseModel):
    status_code: int
    content_type: str
    body: dict
```

BaseModel needs to be imported.

```
from pydantic import BaseModel
```

### Step 6 - Add the Controller

Add [controller.py](src/controller.py) to your code.

cp ../src/controller.py src

### Step 7 - Modify the View

Modify main.py by replacing get_quote_id's implementation with the following.



## Test & Validation

```
bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quote](http://127.0.0.1:8000/quote).
