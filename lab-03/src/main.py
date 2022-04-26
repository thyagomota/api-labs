# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-04-26T20:55:50+00:00

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI

from .models import Quote
from .controller import Controller

app = FastAPI(
    title='Quotes API',
    version='1.0',
)


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