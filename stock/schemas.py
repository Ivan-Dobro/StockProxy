from pydantic import BaseModel
from datetime import date, time, datetime

class StockIn(BaseModel):
    currency: str 
    stk_date: date
    time_frame: str
    stk_open: float
    stk_high: float
    stk_low: float
    stk_close: float