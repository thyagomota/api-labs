# generated by fastapi-codegen:
#   filename:  quotes.yaml
#   timestamp: 2022-04-24T20:47:49+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Quote(BaseModel):
    text: str
    author: str
    tags: List[str]
