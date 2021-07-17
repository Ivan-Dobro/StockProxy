from sqlalchemy.orm import Session
from . import models,schemas
from datetime import  datetime as _dt


def add_in_stock(db:Session, stock_in: schemas.StockIn):

    new_stock = models.Stock(
        currency = stock_in.currency,
        date = _dt.strptime(stock_in.date,'%Y.%m.%d_%H:%M'),
        frame = stock_in.frame,
        open = stock_in.open,
        high = stock_in.high,
        low = stock_in.low,
        close = stock_in.close,
    )
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

