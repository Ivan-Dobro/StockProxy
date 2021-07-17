from pydantic import BaseModel,validator
from datetime import date, time, datetime
from typing import Optional

from sqlalchemy.sql.sqltypes import Boolean




class Stock(BaseModel):
    currency: str 
    date: datetime
    frame: str
    open: float
    high: float
    low: float
    close: float

class StockIn(Stock):
    date: str

class StockOut(BaseModel):
    id: Optional[int]
    is_send: Optional[bool]
    date_created: Optional[datetime]
    currency: Optional[str] 
    date: Optional[datetime]
    frame: Optional[str]
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    class Config():
        orm_mode= True

class StockUpdate(BaseModel):
    is_send: Optional[bool]
    currency: Optional[str]
    date: Optional[datetime]
    frame: Optional[str]
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    # class Config():
    #     orm_mode= True

    # @validator("stk_date", pre=True)
    # def parse_date(cls,v):
    #     # # v = datetime.strftimestr(v)
    #     # print (f' ----------- {v=} -------')
    #     return datetime.strptime(v,"%Y%m%d").date()