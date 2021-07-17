from sqlalchemy import Column,Integer,Numeric, String,DateTime, Boolean, Numeric,Float
from .database import Base
from datetime import datetime as _dt


now = _dt.strptime(_dt.now().isoformat(' ', 'seconds'),'%Y-%m-%d %H:%M:%S')

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer,primary_key = True, index = True)
    is_send = Column(Boolean,default=False)
    date_created = Column(DateTime,default=now)
    currency = Column(String)
    date = Column(DateTime)
    frame = Column(String)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
