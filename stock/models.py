from sqlalchemy import Column,Integer,Float, String,Date, Boolean
from .database import Base

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer,primary_key = True, index = True)
    is_send = Column(Boolean,default=False)
    currency = Column(String)
    stk_date = Column(Date)
    time_frame = Column(String)
    stk_open = Column(Float)
    stk_high = Column(Float)
    stk_low = Column(Float)
    stk_close = Column(Float)
