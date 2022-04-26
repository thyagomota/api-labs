from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from .models import Quote

class Controller: 

  engine = None

  @staticmethod
  def get_engine():
    if not Controller.engine: 
      Controller.engine = create_engine('sqlite:///db/quotes.db')
    return Controller.engine
    
  @staticmethod
  def get_quote():
    engine = Controller.get_engine()
    Session = sessionmaker(engine)
    session = Session()
    quote = session.query(Quote).order_by(func.random()).first()
    print(type(quote))
    return quote

# print(Controller.get_quote().toJSON())
