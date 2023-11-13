from fastapi import  FastAPI
import models
from database import engine
from routes.user import auth,product,category,order

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)