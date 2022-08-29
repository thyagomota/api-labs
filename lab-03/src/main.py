# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-08-29T16:13:10+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from .models import Quote
from fastapi import Response
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from .db_helper import DBHelper

app = FastAPI(
    title='Quotes API',
    version='1.0',
)


@app.get('/quotes', response_model=List[dict], responses={'404': {'model': str}})
def get_quotes(
    text: Optional[str] = None,
    author: Optional[str] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
    popularity: Optional[float] = None,
) -> Union[List[Quote], str]:
    """
    Returns a list of quotes that satisfy a search criteria
    """
    engine = DBHelper.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    if text: 
      result = result.filter(Quote.text.contains(text))
    if author:
      result = result.filter(Quote.author.contains(author))
    if category: 
      result = result.filter(Quote.category == category)
    if popularity: 
      result = result.filter(Quote.popularity >= float(popularity))
    if tag: 
      result = result.filter(Quote.tags.any(tag=tag))
    return [r.__dict__ for r in result]

@app.get('/quotes/{id}', response_model=dict, responses={'404': {'model': str}})
def get_quotes_id(id: int) -> Union[dict, str]:
    """
    Returns a quote given its id; for a random quote use id=0
    """
    engine = DBHelper.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    result = session.query(Quote)
    quote = result.order_by(func.random()).first() if id == 0 else result.get(id)
    return quote.__dict__
