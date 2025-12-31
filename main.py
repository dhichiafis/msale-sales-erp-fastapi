from fastapi import FastAPI,Depends,HTTPException
from routes.users import users_router
from routes.transactions import transaction_router
from routes.role import roles_router
from routes.products import product_router
from routes.purchase import purchase_router
from routes.bonuses import bonus_router
from routes.accounts import accounts_router
from fastapi.middleware.cors import CORSMiddleware
from database import *
from sqlalchemy.orm import Session
from models.model import *
from contextlib import asynccontextmanager
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import settings  # your DB_URL from env


'''
max_tries = 10
for i in range(max_tries):
    try:
        engine = create_engine(settings.DB_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Database is ready!")
        break
    except OperationalError:
        print(f"Waiting for database... ({i+1}/{max_tries})")
        time.sleep(3)
else:
    raise Exception("❌ Could not connect to the database after several attempts")


Base.metadata.create_all(bind=engine)
'''



def seed_accounts(db):
    account_names=['Cash Account','Bank Deposit','Cash Reward']
    account_types=['Asset','Liability','Expense']
    for name,type in zip(account_names,account_types):
        account=db.query(Account).filter(Account.name==name).first()
        if not account:
            account=Account(
                name=name,
                balance=0.0,
                type=type
            )
            db.add(account)
    db.commit()


def seed_roles(db):
    roles=['admin','customer','relation manager']
    for role in roles:
        db_role=db.query(Role).filter(Role.name==role).first()
        if not db_role:
            role_db=Role(name=role)
            db.add(role_db)
    db.commit()

@asynccontextmanager
async def lifespan(app:FastAPI):
    db=SessionFactory()
    seed_roles(db=db)
    seed_accounts(db=db)
    yield 
    db.close()

app=FastAPI(
    lifespan=lifespan,
    title="Msale",description="This is backend app that manages the sales of products and ensures that the correpondeces get rewarded based on the interaction with the rm and the product they bought")
#app.add_middleware(
 #  allow_headers=['*'],
  ## allow_credentials=True 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",],  # must match Vue dev URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(transaction_router)
app.include_router(accounts_router)
app.include_router(roles_router)
app.include_router(product_router)
app.include_router(purchase_router)
app.include_router(bonus_router)



@app.get('/')
async def home():
    return {'message':'welcome to msale but and get 10 back'}



