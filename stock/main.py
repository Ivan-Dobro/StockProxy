'''
StockProxy 
v. 0.1
ivan@dobrokhotov.com

'''

from typing import List
from fastapi import FastAPI,Depends, Response, status, HTTPException
# from fastapi.templating import Jinja2Templates
from . import models,schemas, crud
from .database import engine,SessionLocal
from sqlalchemy.orm import  Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home():
    return {"data":
            {'name':'Hi Stock!'}
            }

@app.get('/stock-in')
def stock_in (stock_in: schemas.StockIn = Depends(), db: Session = Depends(get_db)):

    return crud.add_in_stock(db,stock_in)

@app.get('/stocks-all', response_model=List[schemas.StockOut])
def stock_all(db: Session =Depends (get_db)):
    '''List all stock'''
    stocks = db.query(models.Stock).order_by(models.Stock.date.desc()).all()
    return stocks


@app.get('/fresh/',response_model=schemas.StockOut,status_code=status.HTTP_202_ACCEPTED)
def get_fresh(db: Session = Depends (get_db)):
    '''get stocks with not send'''
    stock = db.query(models.Stock).filter(models.Stock.is_send.is_(False)).order_by(models.Stock.date).first()
    if not stock:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail= f'All stocks where send')
    stock.is_send = True
    db.commit()
    return stock

@app.patch('/update/{id}')
def stock_update(id: int,request: schemas.StockUpdate, db: Session = Depends(get_db)):
    ''' Edit Stock with id'''
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Stock record with id {id} not found !')

    stock.update(request.dict(exclude_unset=True))
    db.commit()
    return f'Updated blog id {id} with {request.dict(exclude_unset=True)}'

@app.patch('/update-all')
def stock_update(request: schemas.StockUpdate, db: Session = Depends(get_db)):
    ''' Edit many Stocks '''
    stocks = db.query(models.Stock).all()
    if not stocks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Stock record with id {id} not found !')
    for item in stocks:
        item = request.dict(exclude_unset=True)
    db.commit()
    return f'Updated blogs with {request.dict(exclude_unset=True)}'


@app.delete('/delete/{id}')
def delete_stock(id: int,db: Session = Depends(get_db)):
    '''Delete Stock with id'''
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock record with id {id} not found")
    stock.delete(synchronize_session=False)
    db.commit()
    return f'Stock with id {id} deleted'
