# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-04-27T21:51:23+00:00

from __future__ import annotations

from fastapi import FastAPI

from .models import Quotes0GetResponse
from .controller import Controller

# NOTE: following import statement has been added
from .controller import Controller

app = FastAPI(
    version='1.0',
    title='Quotes API',
)


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
    
