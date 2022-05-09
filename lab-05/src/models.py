# coding: utf-8
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Key(Base):
    __tablename__ = 'keys'

    key = Column(String(32), primary_key=True)


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=False)
    author = Column(String(100), nullable=False)
    popularity = Column(DECIMAL(7, 2))
    category = Column(String(100))

    # NOTE: following statement has been added
    tags = relationship("QuoteTag", primaryjoin="Quote.id==QuoteTag.id") 

    # NOTE: following method has been added
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

t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class QuoteTag(Base):
    __tablename__ = 'quote_tags'

    id = Column(ForeignKey('quotes.id'), primary_key=True, nullable=False)
    tag = Column(String(30), primary_key=True, nullable=False)

    # NOTE: following statement has been commented out
    # quote = relationship('Quote')
