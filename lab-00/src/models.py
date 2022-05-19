# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-05-19T20:23:07+00:00

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel

class Quote(BaseModel):
    id: int
    text: str
    author: str
    popularity: Optional[float] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class Quotes0GetResponse(BaseModel):
    status_code: int
    content_type: str
    body: Quote
