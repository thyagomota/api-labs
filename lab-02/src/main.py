# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-04-28T17:33:51+00:00

from __future__ import annotations

from typing import Union

from fastapi import FastAPI

# NOTE: following import statement has been modified
from .models import Quote

# NOTE: following import statement has been added
from .controller import Controller

app = FastAPI(
    title='Quotes API',
    version='1.0',
)

# NOTE: following method has been modified
@app.get('/quotes/{id}')
def get_quotes_id(id: int) -> Quote:
    quote = Controller.get_quote(id)
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
            'body': 'Not Found'
        } 