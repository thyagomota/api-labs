# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-05-26T21:32:24+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from .models import Quote

from fastapi import Response
from .controller import Controller

app = FastAPI(
    title='Quotes API',
    version='1.0',
)


# @app.get('/quotes', response_model=List[Quote], responses={'404': {'model': str}})
# def get_quotes(
#     text: Optional[str] = None,
#     author: Optional[str] = None,
#     category: Optional[str] = None,
#     tag: Optional[str] = None,
#     popularity: Optional[float] = None,
# ) -> Union[List[Quote], str]:
#     """
#     Returns a list of quotes that satisfy a search criteria
#     """
#     pass

@app.get('/quotes', response_model=list)
def get_quotes(
    response: Response,
    text: Optional[str] = None,
    author: Optional[str] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    popularity: Optional[float] = None) -> List[Quote]:
    """
    Returns a list of quotes that satisfy a search criteria
    """
    quotes = Controller.get_quotes(text, author, category, tag, popularity)
    print(quotes)
    if quotes:
        response.status_code = 200
    else:
        response.status_code = 404
    return quotes

# @app.get('/quotes/{id}', response_model=Quote, responses={'404': {'model': str}})
# def get_quotes_id(id: int) -> Union[Quote, str]:
#     """
#     Returns a quote given its id; for a random quote use id=0
#     """
#     pass

@app.get('/quotes/{id}', response_model=dict)
def get_quotes_id(id: int, response: Response) -> Quote:
    """
    Returns a quote given its id; for a random quote use id=0
    """
    quote = Controller.get_quotes_id(id)
    print(quote)
    if quote:
        response.status_code = 200
        return quote.__dict__
    else:
        response.status_code = 404
        return {'message': 'Not Found!'}
